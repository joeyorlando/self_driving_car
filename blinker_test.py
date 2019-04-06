import time
import RPi.GPIO as GPIO
from hardware.blinker import Blinker

GPIO.setmode(GPIO.BOARD)

b = Blinker(4)
b.start_blinking()
time.sleep(20)
b.stop_blinking()