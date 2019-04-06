import time
import RPi.GPIO as GPIO

class Blinker:

	def __init__(self, pin):
		self.pin = pin
		self.blinking = False
		GPIO.setup(self.pin, GPIO.OUT)

	def start_blinking(self):
		self.blinking = True
		while self.blinking:
			GPIO.output(self.pin, GPIO.HIGH)
			time.sleep(0.8)
			GPIO.output(self.pin, GPIO.LOW)
			time.sleep(0.8)

	def stop_blinking(self):
		self.blinking = False