import RPi.GPIO as GPIO
import math
import time

GPIO.setmode(GPIO.BCM)
GPIO18 = 18
GPIO.setup(GPIO18, GPIO.OUT)

p18 = GPIO.PWM(GPIO18, 60)#GPIO, frequency
p18.start(0)
i = 0
try:
    while True:
        i += 1
        p18.ChangeDutyCycle(50 * math.sin(0.1 * i) + 50)
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
p18.stop()
GPIO.cleanup()
