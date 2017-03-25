import RPi.GPIO as GPIO
from lib.config import config
GPIO.setmode(GPIO.BOARD)


class Motor:


	def __init__(self):
		pin_forward = config["hardware_pins"]["motor"]["forward"]
		pin_backward = config["hardware_pins"]["motor"]["backward"]
		pin_straight = config["hardware_pins"]["motor"]["straight"]
		pin_steering = config["hardware_pins"]["motor"]["steering"]
		pin_right = config["hardware_pins"]["motor"]["right"]
		pin_left = config["hardware_pins"]["motor"]["left"]

		GPIO.setup(pin_forward, GPIO.OUT)
		GPIO.setup(pin_backward, GPIO.OUT)
		GPIO.setup(pin_straight, GPIO.OUT)
		GPIO.setup(pin_steering, GPIO.OUT)
		GPIO.setup(pin_right, GPIO.OUT)
		GPIO.setup(pin_left, GPIO.OUT)

		self.pwm_forward = GPIO.PWM(pin_forward, 100)
		self.pwm_backward = GPIO.PWM(pin_backward, 100)
		self.pwm_forward.start(0)
		self.pwm_backward.start(0)

		self.pwm_left = GPIO.PWM(pin_left, 100)
		self.pwm_right = GPIO.PWM(pin_right, 100)
		self.pwm_left.start(0)
		self.pwm_right.start(0)

		GPIO.output(pin_straight, GPIO.HIGH)
		GPIO.output(pin_steering, GPIO.HIGH)


	def forward(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_backward.ChangeDutyCycle(0)
		self.pwm_forward.ChangeDutyCycle(speed)


	def forward_left(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_backward.ChangeDutyCycle(0)
		self.pwm_forward.ChangeDutyCycle(speed)
		self.pwm_right.ChangeDutyCycle(0)
		self.pwm_left.ChangeDutyCycle(100)


	def forward_right(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_backward.ChangeDutyCycle(0)
		self.pwm_forward.ChangeDutyCycle(speed)
		self.pwm_left.ChangeDutyCycle(0)
		self.pwm_right.ChangeDutyCycle(100)


	def backward(self, speed):
		"""
			pinBackward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_forward.ChangeDutyCycle(0)
		self.pwm_backward.ChangeDutyCycle(speed)


	def left(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_right.ChangeDutyCycle(0)
		self.pwm_left.ChangeDutyCycle(speed)


	def right(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		self.pwm_left.ChangeDutyCycle(0)
		self.pwm_right.ChangeDutyCycle(speed)


	def stop(self):
		""" Set the duty cycle of both control pins to zero to stop the motor. """
		self.pwm_forward.ChangeDutyCycle(0)
		self.pwm_backward.ChangeDutyCycle(0)
		self.pwm_left.ChangeDutyCycle(0)
		self.pwm_right.ChangeDutyCycle(0)
