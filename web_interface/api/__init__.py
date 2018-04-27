import os
from flask import Flask, request, render_template, Response
from hardware.car import Car

web_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../web'))
template_folder = "%s/templates" % web_folder
static_folder = "%s/static" % web_folder

api = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
car = Car()


@api.route("/", methods=["GET"])
def get_webpage():
	return render_template('index.html')

@api.route("/video_feed", mtehods=["GET"])
def get_video_stream():
	"""
		https://blog.miguelgrinberg.com/post/video-streaming-with-flask
	"""
	return Response(car.camera.stream(), mimetype="multipart/x-mixed-replace; boundary=frame")

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