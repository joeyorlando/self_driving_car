import os
import time
from flask import Flask, request, render_template, Response, jsonify
from hardware.car import Car

template_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), './templates'))
static_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), './static'))

api = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder)
car = Car()
recording = False
output_data_folder_name = "./data/training/%s" % int(time.time())

os.system("mkdir %s" % output_data_folder_name)
print("FOLDER NAME IS %s" % output_data_folder_name)


@api.route("/", methods=["GET"])
def get_webpage():
    return render_template('index.html')


@api.route("/video_feed", methods=["GET"])
def get_video_stream():
    """
            https://blog.miguelgrinberg.com/post/video-streaming-with-flask
    """
    return Response(car.camera.stream(output_data_folder_name), mimetype="multipart/x-mixed-replace; boundary=frame")


@api.route("/drive", methods=["POST"])
def drive_the_car():
    request_body = request.get_json()
    command = request_body.get("command")

    if '37' in command:
        car.turn_left()
    elif '38' in command:
        car.drive_forward()
    elif '39' in command:
        car.turn_right()
    elif '40' in command:
        car.drive_backward()
    # else:
    # 	car.stop()

    return 'Ok'


@api.route("/start_recording", methods=["POST"])
def start_recording():
    global recording
    recording = True
    return 'Ok'


@api.route("/stop_recording", methods=["POST"])
def stop_recording():
    global recording
    recording = False
    return 'Ok'
