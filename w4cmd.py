>>> import RPi.GPIO as GPIO
>>> import time
>>> GPIO.setmode(GPIO.BOARD)
>>> GPIO.setup(12,GPIO.OUT)
__main__:1: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
>>> pwm=GPIO.PWM(12,50)
>>> pwm.start(0)
>>> while(True):
...     for i in range(100):
...             pwm.ChangeDutyCycle(i)
...             time.sleep(0.1)
...     for i in range(100,0,-1):
...             pwm.ChangeDutyCycle(i)
...             time.sleep(0.1)
... 
