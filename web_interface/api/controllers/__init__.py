from api import api
from flask import request, render_template
from hardware.car import Car

car = Car()


@api.route("/", methods=["GET"])
def get_webpage():
	return render_template('index.html')


@api.route("/drive", methods=["POST"])
def drive_the_car():
	request_body = request.get_json()
	command = request_body.get("command")

	if '37' in command:
		car.forward_left(100)
	elif '38' in command:
		car.forward(100)
	elif '39' in command:
		car.forward_right(100)
	elif '40' in command:
		car.backward(100)
	else:
		car.stop()


@api.route("/store_logs", methods=["GET"])
def store_logs():
	pass
