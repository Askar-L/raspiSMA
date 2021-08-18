import time
import RPi.GPIO as GPIO
LED = 12 #Physical pin 7, BCM pin GPIO.4 on the BCM2835
# GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM
GPIO.)
GPIO.setup(LED, GPIO.OUT)#pull_up_down=GPIO.PUD_UP
idx = 0
hold = 0.05
GPIO.output(LED, 0)
sign = True
# while True: 
    # idx+=1
    # print("GOING!!:{}".format(idx))
    # time.sleep(hold)
    # GPIO.output(LED, sign)
    # sign = not sign
    # print(sign)

while idx < 30:
    idx+=1
    GPIO.setup(LED, GPIO.OUT)#pull_up_down=GPIO.PUD_UP
    print("Light!!:{}".format(idx))
    GPIO.output(LED, True)
    time.sleep(hold)
    GPIO.output(LED, False)
    # time.sleep(0.1)
    
GPIO.cleanup()
# https://cae2100.wordpress.com/2013/01/10/short-tutorial-on-raspberry-pis-gpio-pins-in-python/