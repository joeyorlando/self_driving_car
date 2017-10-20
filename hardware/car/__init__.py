import RPi.GPIO as GPIO
from hardware.car.motor import Motor
from hardware.range_sensor import RangeSensor
# from hardware.camera import Camera

GPIO.setmode(GPIO.BOARD)


class Car:


	def __init__(self):
		self.rear_motor = Motor(motor_type="rear_motor")
		self.front_motor = Motor(motor_type="front_motor")
		# self.range_sensor = RangeSensor()
		# self.camera = Camera()


	def drive_forward(self):
		self.front_motor.forward(1)


	def drive_backward(self):
		self.front_motor.backward(1)


	def stop(self):
		self.front_motor.stop()
