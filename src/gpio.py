'''
Created on 02-Oct-2016
@author: ramit
'''
#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys, getopt

def gpio(pin):
    pin = int(pin)
    switcher = {
        2: 3,3: 5,4: 7,5: 29,6: 31,7: 26,8: 24,9: 21,10: 19,11: 23,12: 32,13: 33,14: 8,15: 10,16: 36,17: 11,18: 12,19: 35,20: 38,21: 40,22: 15,23: 16,24: 18,25: 22,26: 37,27: 13,
    }
    return switcher.get(pin, "false")

def main(argv):
    gpiopin = ''
    status = ''
    type = 'pin'
    try:
        GPIO.setmode(GPIO.BOARD)
        opts, args = getopt.getopt(argv,"hg:s:t:",["gpio=","status=","type="])
    except getopt.GetoptError:
        print 'gpio.py -g <number> -s <status> -t <pin/gpio>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'gpio.py -g <number> -s <status> -t <pin/gpio>'
            sys.exit()
        elif opt in ("-g", "--gpio"):
            gpiopin = arg
        elif opt in ("-s", "--status"):
            status = arg
        elif opt in ("-t", "--type"):
            type = arg
    if gpiopin != "":
        print 'GPIO is "', gpiopin
        print 'Status is "', status
        print 'type is "', type
        gpiopin=int(gpiopin)
        status=int(status)
        GPIO.setwarnings(False)
        if type=='gpio':
            gpiopin=gpio(gpiopin)
        GPIO.setup(gpiopin, GPIO.OUT)
        GPIO.output(gpiopin,status)
        if status == 0:
            GPIO.cleanup()
    else:
        print 'gpio.py -g <number> -s <status> -t <pin/gpio>'
    
if __name__ == "__main__":
    main(sys.argv[1:])