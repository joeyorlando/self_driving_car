import RPi.GPIO as GPIO
from hardware.car.motor import Motor
from hardware.range_sensor import RangeSensor
from hardware.camera import Camera

GPIO.setmode(GPIO.BOARD)


class Car:


	def __init__(self):
		self.rear_motor = Motor(motor_type="rear_motor")
		self.front_motor = Motor(motor_type="front_motor")
		self.range_sensor = RangeSensor()
		self.camera = Camera()


	def drive_forward(self):
		GPIO.output(self.rear_motor.input2, GPIO.HIGH)
		GPIO.output(self.rear_motor.input1, GPIO.LOW)
		GPIO.output(self.rear_motor.enable, GPIO.HIGH)


	def drive_backward(self):
		GPIO.output(self.rear_motor.input2, GPIO.LOW)
		GPIO.output(self.rear_motor.input1, GPIO.HIGH)
		GPIO.output(self.rear_motor.enable, GPIO.HIGH)


	def stop(self):
		GPIO.output(self.rear_motor.enable, GPIO.LOW)
