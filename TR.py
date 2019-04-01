import time
import sys
import RPi.GPIO as GPIO

left='1111111111111010101011101'
right='1111111111101110101011101'
forward='1111111111101011101011101'
backward='1111111111101010111011101'
neutral='1111111111101010111010111'
short_delay=0.00045
long_delay=0.00090
extended_delay=0.0096

NUM_ATTEMPTS=10
TRANSMIT_PIN=23

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN,GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i=='1':
                GPIO.output(TRANSMIT_PIN,1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN,0)
                time.sleep(long_delay)
            elif i=='0':
                GPIO.output(TRANSMIT_PIN,1)
                time.slep(long_delay)
                GPIO.output(TRANSMIT_PIN,0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN,0)
        time.sleep(extended_delay)
    GPIO.cleanup()
if__name__ =='__main__':
    for argument kin sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
