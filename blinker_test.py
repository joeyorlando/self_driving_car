import time
import RPi.GPIO as GPIO
from hardware.blinker import Blinker

GPIO.setmode(GPIO.BOARD)

b = Blinker(7)

for _ in range(5):
	b.blink()