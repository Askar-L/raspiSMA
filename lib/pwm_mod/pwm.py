import RPi.GPIO as GPIO,time

class PWM(object):
    def __init__(self,channel,mode) -> None:
        super(PWM).__init__()
        # GPIO.cleanup()
        
        self.duty = 0
        self.mode = str(mode.upper())
        self.channel = int(channel)

        if mode.upper() == "BCM": 
            GPIO.setmode(GPIO.BCM)
            if channel < 1 or channel >26: print("BCM Chaanel wrong! exit....");exit()
        elif mode.upper() == "BOARD": 
            GPIO.setmode(GPIO.BOARD)
            if channel < 1 or channel >40: print("BOARD Chaanel wrong! exit....");exit()
        else : print("MODE is not correct!"); exit()
        
        GPIO.setup(channel, GPIO.OUT)
        self.pwm = GPIO.PWM(self.channel,5) # 5 Hz
        print("The pwm wave is initialized on mode: {} at channel: {}".format(self.mode,self.channel))

        self.pwm.start(100) # duty 100
        self.pwm.ChangeFrequency(5) # 5 Hz
        time.sleep(10)
        self.pwm.stop()

    def blink(self,freq,brightness,lasting):
        print("Blinking for {} sec".format(lasting))
        self.pwm.start(brightness)
        # self.pwm.ChangeDutyCycle(brightness)
        self.pwm.ChangeFrequency(freq)

        time.sleep(lasting)
        self.pwm.stop()
        # while run_time < lasting:

    def test(self):
        pwm = GPIO.PWM(self.channel,3000)
        print("Light 30%")
        pwm.start(30)
        time.sleep(2)
        print("Blink!")
        # while True:
        pwm.ChangeFrequency(4)
        pwm.ChangeDutyCycle(50)
        # pwm.start(80)
        time.sleep(2)
        print("OFF!")
        pwm.ChangeDutyCycle(0)
        pass

    def breath(self,time,frequncy)-> None:
        if frequncy == 0: pass
        else:
            T = 1/frequncy
        

    def close(self):
        GPIO.cleanup()