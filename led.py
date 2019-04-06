import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_pin, GPIO.OUT)

for _ in range(10):
	GPIO.output(led_pin, GPIO.HIGH)
	time.sleep(0.8)
	GPIO.output(led_pin, GPIO.LOW)
	time.sleep(0.8)
