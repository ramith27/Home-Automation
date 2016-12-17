#!/usr/bin/env python
'''
Created on 07-Nov-2016
Updated on 16-Dec-2016
@author: Ramith Nambiar
Version : 1.5
'''
import RPi.GPIO as GPIO
import sys, getopt,requests,json,time
import urllib2,cookielib
from urllib2 import URLError

user="xxxxxxxxxxx"
hash="xxxxxxxxxxx"
url="http://iotcon.top/connect.json"

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

url=url+"?user="+user+"&serial="+serial+"&hash="+hash
while True :
    time.sleep(10)
    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    
    try:
        response = urllib2.urlopen(req)
        gpiostatus = json.load(response)
        try:
            gpiostatus['Raspberry']
            for val in gpiostatus['Raspberry']:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setwarnings(False)
                gpiopin=int(val['pin_no'])
                GPIO.setup(gpiopin, GPIO.OUT)
                GPIO.output(gpiopin,int(val['pin_status']))
        except Exception, e:
            print "User Id : " +user
            print "Hash : " +hash
            print "Error : "+gpiostatus['Error']
            sys.exit()
    except URLError, error:
        print "Error Occured"
        time.sleep(100)
