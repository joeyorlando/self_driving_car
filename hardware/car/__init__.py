from hardware.car.motor import Motor
from hardware.car.range_sensor import RangeSensor
from hardware.car.camera import Camera

class Car(Motor):


	def __init__(self):
		Motor.__init__(self)
		self.range_sensor = RangeSensor()
		self.camera = Camera()
