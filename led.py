#coding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)#GPIO番号で指定
#GPIO.setmode(GPIO.BOARD)#ピン番号で指定

GPIO18 = 18
GPIO.setup(GPIO18, GPIO.OUT)
try:
    while True:
        GPIO.output(GPIO18, True)
        time.sleep(1)
        GPIO.output(GPIO18, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
