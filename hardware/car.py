import RPi.GPIO as GPIO
from hardware.motor import Motor
from hardware.range_sensor import RangeSensor
from hardware.camera import Camera
from hardware.blinker import Blinker


class Car:

	def __init__(self):
		self.rear_motor = Motor(motor_type="rear_motor")
		self.front_motor = Motor(motor_type="front_motor")
		
		self.front_right_blinker = Blinker(7)
		self.fron_left_blinker = Blinker(11)		
		
		self.range_sensor = RangeSensor()
		self.camera = Camera()

	def drive_forward(self):
		self.rear_motor.forward(0.1)

	def drive_backward(self):
		self.rear_motor.backward(0.1)

	def turn_left(self):
		self.front_motor.forward(0.1)

	def turn_right(self):
		self.front_motor.backward(0.1)

	def stop(self):
		self.rear_motor.stop()
