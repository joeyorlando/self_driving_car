import RPi.GPIO as GPIO
from lib.config import config
GPIO.setmode(GPIO.BOARD)


class Motor:


	def __init__(self, motor_type):
		enable = config["hardware_pins"][motor_type]["enable"]
		pin_backward = config["hardware_pins"][motor_type]["input1"]
		pin_forward = config["hardware_pins"][motor_type]["input2"]

		# pin_forward = config["hardware_pins"]["motor"]["forward"]
		# pin_backward = config["hardware_pins"]["motor"]["backward"]
		# pin_straight = config["hardware_pins"]["motor"]["straight"]
		# pin_steering = config["hardware_pins"]["motor"]["steering"]
		# pin_right = config["hardware_pins"]["motor"]["right"]
		# pin_left = config["hardware_pins"]["motor"]["left"]

		for pin in [enable, pin_backward, pin_forward]:
			GPIO.setup(pin, GPIO.OUT)

		# Pulse width modulation
		self.pwm_forward = GPIO.PWM(pin_forward, 100)
		self.pwm_backward = GPIO.PWM(pin_backward, 100)

		for pwm in [self.pwm_forward, self.pwm_backward]:
			pwm.start(0)

		GPIO.output(enable, GPIO.HIGH)


	def forward(self, speed):
		"""
			pinForward is the forward Pin, so we change its duty cycle according to speed
		"""
		GPIO.output(self.pin_backward, GPIO.HIGH)
		GPIO.output(self.pin_forward, GPIO.LOW)
		GPIO.output(self.enable, GPIO.HIGH)
		# self.pwm_backward.ChangeDutyCycle(0)
		# self.pwm_forward.ChangeDutyCycle(speed)


	# def forward_left(self, speed):
	# 	"""
	# 		pinForward is the forward Pin, so we change its duty cycle according to speed
	# 	"""
	# 	self.pwm_backward.ChangeDutyCycle(0)
	# 	self.pwm_forward.ChangeDutyCycle(speed)
	# 	self.pwm_right.ChangeDutyCycle(0)
	# 	self.pwm_left.ChangeDutyCycle(100)
	#
	#
	# def forward_right(self, speed):
	# 	"""
	# 		pinForward is the forward Pin, so we change its duty cycle according to speed
	# 	"""
	# 	self.pwm_backward.ChangeDutyCycle(0)
	# 	self.pwm_forward.ChangeDutyCycle(speed)
	# 	self.pwm_left.ChangeDutyCycle(0)
	# 	self.pwm_right.ChangeDutyCycle(100)


	def backward(self, speed):
		"""
			pinBackward is the forward Pin, so we change its duty cycle according to speed
		"""
		GPIO.output(self.pin_forward, GPIO.LOW)
		GPIO.output(self.pin_backward, GPIO.HIGH)
		GPIO.output(self.enable, GPIO.HIGH)
		# self.pwm_forward.ChangeDutyCycle(0)
		# self.pwm_backward.ChangeDutyCycle(speed)


	# def left(self, speed):
	# 	"""
	# 		pinForward is the forward Pin, so we change its duty cycle according to speed
	# 	"""
	# 	self.pwm_right.ChangeDutyCycle(0)
	# 	self.pwm_left.ChangeDutyCycle(speed)
	#
	#
	# def right(self, speed):
	# 	"""
	# 		pinForward is the forward Pin, so we change its duty cycle according to speed
	# 	"""
	# 	self.pwm_left.ChangeDutyCycle(0)
	# 	self.pwm_right.ChangeDutyCycle(speed)
	#
	#
	def stop(self):
		""" Set the duty cycle of both control pins to zero to stop the motor. """
		GPIO.output(self.enable, GPIO.LOW)
		# self.pwm_forward.ChangeDutyCycle(0)
		# self.pwm_backward.ChangeDutyCycle(0)
		# self.pwm_left.ChangeDutyCycle(0)
		# self.pwm_right.ChangeDutyCycle(0)
