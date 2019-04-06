import RPi.GPIO as GPIO
from time import sleep
from hardware.car import Car


GPIO.setmode(GPIO.BOARD)
car = Car()

print("TURN LEFT")
car.turn_left()
sleep(3)

print("TURN RIGHT")
car.turn_right()
sleep(3)

print("STOP")
car.stop()
GPIO.cleanup()
