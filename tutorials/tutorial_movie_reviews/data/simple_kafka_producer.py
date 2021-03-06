#!/usr/bin/env python
#
#  Pass 2 events/lines from file 'sorted_reviews_100000.json' 
#  to kafka per second.
#

from kafka import SimpleProducer, KafkaClient
import time

# kafka client
client    = KafkaClient('localhost:9092')
producer  = SimpleProducer(client)

# data counter
counter   = 0 
timestamp = time.time() 

# data source file
datafile  = open('sorted_reviews_100000.json', 'r')
topic     = 'movie_reviews'

# loop over file and pass events to kafka
for line in datafile:
    # pass reviews to kafka
    try:
        producer.send_messages(topic, line)
        counter +=1
        # status message
        if (counter % 1000)==0: 
            now = time.time()
            print str(counter)+' events sent in '+str(now-timestamp)+' seconds: '+str(1000.0/(now-timestamp))+' evts/sec'
            timestamp = now
    except:
        print 'New topic created, or something went wrong.'
    # SLEEP 1/2 second
    time.sleep(0.5)

##############################################################
