'''
Created on 07-Nov-2016
@author: Ramith Nambiar
Version : 1.0
'''

#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys, getopt,requests,json,time

user="XXXXXXXXXX"
hash="XXXXXXXXXX"

def gpio(pin):
    pin = int(pin)
    switcher = {
        2: 3,3: 5,4: 7,5: 29,6: 31,7: 26,8: 24,9: 21,10: 19,11: 23,12: 32,13: 33,14: 8,15: 10,16: 36,17: 11,18: 12,19: 35,20: 38,21: 40,22: 15,23: 16,24: 18,25: 22,26: 37,27: 13,
    }
    return switcher.get(pin, "false")

while True :
    time.sleep(120) #Every 2 Min . Dont Chnage The Value .If changed time you may get banned
    url = 'http://we4u.pw/iot/connect.html?user='+user+'&hash='+hash
    r = requests.get(url)
    gpiostatus=r.json();
    for val in gpiostatus['Raspberry']:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        gpiopin=int(val['gpio_no'])
        gpiopin=gpio(gpiopin)
        GPIO.setup(gpiopin, GPIO.OUT)
        GPIO.output(gpiopin,val['gpio_status'])
