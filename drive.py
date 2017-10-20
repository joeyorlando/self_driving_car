import RPi.GPIO as GPIO
from time import sleep
from hardware.car import Car

car = Car()

print("FORWARD MOTION")
car.drive_forward()
sleep(0.5)

print("BACKWARD MOTION")
car.drive_backward()
sleep(0.5)

print("STOP")
car.stop()
GPIO.cleanup()
