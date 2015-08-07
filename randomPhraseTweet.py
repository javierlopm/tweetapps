#!/usr/bin/env python

# RaspberryPi app
# 
# Developed by Javier Lopez
# 03/22/2015

import tweepy
import sys
import re
import datetime
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

#Make phrase and tweet it
from randomPhrases.makePhrase import *
d = dictionary()

string = "The" + d.makePhraseFromCode(["A","N","t"]) + " #randomPhrase"

status = api.update_status(status=string)
