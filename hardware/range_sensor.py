import RPi.GPIO as GPIO
from lib.config import config
GPIO.setmode(GPIO.BOARD)


class RangeSensor:


	def __init__(self):
		GPIO.setup(config["hardware_pins"]["range_sensor"]["trig"], GPIO.OUT)
		GPIO.setup(config["hardware_pins"]["range_sensor"]["echo"], GPIO.IN)
