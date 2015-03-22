#!/usr/bin/env python

# RaspberryPi app
# 
# Developed by Javier Lopez
# 03/22/2015

from twython import Twython
import sys
import re
import datetime
import subprocess



#Temp check, Raspberry Pi only
status = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
m      = re.search('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',status)

temp = float(m.group(0))

#Messages according to temp, if less than 40, exit and don't tweet about it
if  (40 <= temp and temp<50):
    string = 'Hey...'
elif(50 <= temp and temp<60):
    string = 'Subiendo'
elif(60 <= temp):
    string = 'Dude @javierlopm hace calor aqui'
else:
    exit()


#Reading keys under the password file 
keys = open('password','r')
consumerKey         = keys.readline()[:-1]
consumerSecret      = keys.readline()[:-1]
acessToken          = keys.readline()[:-1]
acessTokenSecret    = keys.readline()[:-1]
keys.close()

#Twython init
twitter = Twython(consumerKey, consumerSecret,acessToken, acessTokenSecret)
twitter.verify_credentials()

#Tweet temperature, according to the hour (Spanish hour word pick)
if(string,datetime.datetime.now().strftime('%I') == '01' ):
    string = "{0} a la {1} estoy a {2} C".format(
                                    string,
                                    datetime.datetime.now().strftime('%I:%M'),
                                    float(m.group(0))
                                                )
else:
    string = "{0} a las {1} estoy a {2} C".format(
                                    string,
                                    datetime.datetime.now().strftime('%I:%M'),
                                    float(m.group(0))
                                                  )

status = twitter.update_status(status=string)
