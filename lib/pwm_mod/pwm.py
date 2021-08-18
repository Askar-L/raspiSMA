import RPi.GPIO as GPIO,time

class PWM(object):
    def __init__(self,channel,mode) -> None:
        super(PWM).__init__()
        self.duty = 0
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)

    def breath(self,time,frequncy)-> None:
        if frequncy == 0: pass
        else:
            T = 1/frequncy
        

    def close(self):
        GPIO.cleanup()