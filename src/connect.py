#!/usr/bin/env python
'''
Created on 07-Nov-2016
Updated on 16-Dec-2016
@author: Ramith Nambiar
@website: www.iotcon.top
Version : 1.6
'''
import RPi.GPIO as GPIO
import sys, getopt,requests,json,time
import urllib2,cookielib
from urllib2 import URLError

user="xxxxxxxxxxxxx"
hash="xxxxxxxxxxxxx"
url="http://iotcon.top/api/client/v2/json"

def getserial():
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial

serial=getserial()
print "Serial Number : "+serial

def gpio(pin):
    pin = int(pin)
    switcher = {
        2: 3,3: 5,4: 7,5: 29,6: 31,7: 26,8: 24,9: 21,10: 19,11: 23,12: 32,13: 33,14: 8,15: 10,16: 36,17: 11,18: 12,19: 35,20: 38,21: 40,22: 15,23: 16,24: 18,25: 22,26: 37,27: 13,
    }
    return switcher.get(pin, "false")

def pin(gpio):
    gpio = int(gpio)
    switcher = {
        3: 2,5: 3,7: 4,29: 5,31: 6,26: 7,24: 8,21: 9,19: 10,23: 11,32: 12,33: 13,8: 14,10: 15,36: 16,11: 17,12: 18,35: 19,38: 20,40: 21,15: 22,16: 23,18: 24,22: 25,37: 26,13: 27,
    }
    return switcher.get(gpio, "false")

url=url+"/ajax/"+serial+"/view?user="+user+"&hash="+hash+"&connect=1"

while True :
    time.sleep(2)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)

    try:
        response = urllib2.urlopen(req)
        gpiostatus = json.load(response)
        if gpiostatus['success']==True:
            try:
                result=gpiostatus['result']
                for val in result['raspberry']:
                    print gpiostatus
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setwarnings(False)
                    gpiopin=int(val['pin_no'])
                    GPIO.setup(gpiopin, GPIO.OUT)
                    GPIO.output(gpiopin,int(val['pin_status']))
            except Exception, e:
                print str(e)
                print "User Id : " +user
                print "Hash : " +hash
                print "Error : "+gpiostatus['error']
                sys.exit()
        else:
            errors=gpiostatus['errors']
            print "=========  Error Occured  ==========="
            print "Error Code  : "+str(errors['code'])
            print "Error Message  : "+str(errors['message'])
            time.sleep(100)

    except URLError, error:
        print "Error Occured"
        time.sleep(100)
