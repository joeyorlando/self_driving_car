import time
import RPi.GPIO as GPIO


class Blinker:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.8)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.8)
