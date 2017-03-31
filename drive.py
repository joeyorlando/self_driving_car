import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1 = 16    # Input Pin
Motor2 = 18    # Input Pin
Motor3 = 22    # Enable Pin

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

print("BACKWARD MOTION")
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)

sleep(3)

print("FORWARD MOTION")
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)

sleep(3)

print("STOP")
GPIO.output(Motor3,GPIO.LOW)

GPIO.cleanup()
