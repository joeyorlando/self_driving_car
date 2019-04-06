import RPi.GPIO as GPIO
from time import sleep
from hardware.car import Car


GPIO.setmode(GPIO.BCM)
car = Car()

print("FORWARD MOTION")
car.drive_forward()
sleep(10)

print("STOP")
car.stop()
GPIO.cleanup()
