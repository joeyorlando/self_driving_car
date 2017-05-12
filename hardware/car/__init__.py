from hardware.car.motor import Motor
from hardware.car.range_sensor import RangeSensor
from hardware.car.camera import Camera


class Car:


	def __init__(self):
		self.rear_motor = Motor()
		self.front_motor = Motor()
		self.range_sensor = RangeSensor()
		self.camera = Camera()
