import time
import RPi.GPIO as GPIO
frequency = 400
channel = 27 #BCM channel
duty_cycle = 30
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

pwm_duty = 20
if False:
    while idx < 100:
        print(idx)
        pwm = GPIO.PWM(channel,frequency)
        pwm.start(idx)
        time.sleep(4)
        pwm.stop()
        time.sleep(0.4)
        # pwm.ChangeDutyCycle(idx)
        idx += 20

pwm_duty = 50
delta = 1
pwm = GPIO.PWM(channel,frequency)
while pwm_duty <= 100:
    print(pwm_duty)
    pwm.start(pwm_duty)
    time.sleep(0.002)
    # pwm.stop()
    # time.sleep(0.05)
    # pwm.ChangeDutyCycle(idx)
    pwm_duty += delta
    if pwm_duty == 100:         delta = -1
    if pwm_duty == 1:        delta = 1
    break
# while duty_cycle > 0: 
#     duty_cycle -= 10
#     pwm.ChangeDutyCycle(duty_cycle)
#     print(duty_cycle)
#     time.sleep(2)
#     idx+=1
GPIO.cleanup()