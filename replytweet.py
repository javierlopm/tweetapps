#!/usr/bin/env python

# RaspberryPi app
# 
# Developed by Javier Lopez
# 03/22/2015

import tweepy
import sys
import re
from datetime import datetime, timedelta
import subprocess



#reload(sys)
#sys.setdefaultencoding('utf-8')



#Reading keys under the password file 
keys = open('password','r')
consumerKey         = keys.readline()[:-1]
consumerSecret      = keys.readline()[:-1]
acessToken          = keys.readline()[:-1]
acessTokenSecret    = keys.readline()[:-1]
keys.close()

#Tweepy init
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(acessToken, acessTokenSecret)
api = tweepy.API(auth)

"""
class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print('Ran on_status')

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

    def on_data(self, data):
        print(data)
        print('Ok, this is actually running')

l = StreamListener()

streamer = tweepy.Stream(auth=auth, listener=l)
setTerms = ['twitter']
streamer.filter(track = setTerms)
"""

mentions = api.mentions_timeline(count=5)

for tweet in mentions:
    
    postedInLastMinute    = (datetime.now() - timedelta(minutes=1) + timedelta(hours=4,minutes=30) <= tweet.created_at)
    hasHashtags           = len(tweet.entities['hashtags']) != 0
    hasRandomPhraseRequest = False

    if hasHashtags:
        for ht in tweet.entities['hashtags']:
            if ht['text'] == "randomPhrase":
                hasRandomPhraseRequest = True
                break


    #if postedInLastMinute and :
    if postedInLastMinute and hasRandomPhraseRequest:
        from randomPhrases.makePhrase import *
        d = dictionary()
        status = api.retweet(tweet.id)
        string  = "Here you go @%s: " % (tweet.user.screen_name)
        string += "The" + d.makePhraseFromCode(["A","N","t"]) + " #randomPhrase"
        status = api.update_status(status=string)
    


"""

from randomPhrases.makePhrase import *
d = dictionary()

string = "The" + d.makePhraseFromCode(["A","N","t"]) + " #randomPhrase"

status = api.update_status(status=string)
"""
