import RPi.GPIO as io
io.setmode(io.BCM)

in1_pin = 4
in2_pin = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()
	except:
		print("Error writing to: " + property + " value: " + value)

set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")

def clockwise():
	io.output(in1_pin, True)
	io.output(in2_pin, False)

def counter_clockwise():
	io.output(in1_pin, False)
	io.output(in2_pin, True)

clockwise()

while True:
	cmd = input("Command, f/r 0..9, E.g. f5 :")
	direction = cmd[0]
	if direction == "f":
		clockwise()
	else:
		counter_clockwise()
	speed = int(cmd[1]) * 11
	set("duty", str(speed))
