import time
import io
import threading
import picamera


class Camera:
	"""
		https://github.com/miguelgrinberg/flask-video-streaming/blob/v1/camera_pi.py
	"""

	thread = None  # background thread that reads frames from camera
	frame = None  # current frame is stored here by background thread
	last_access = 0  # time of last client access to the camera

	def initialize(self):
		if Camera.thread is None:
			# start background frame thread
			Camera.thread = threading.Thread(target=self._thread)
			Camera.thread.start()

			# wait until frames start to be available
			while self.frame is None:
				time.sleep(0)

	def get_frame(self):
		Camera.last_access = time.time()
		self.initialize()
		return self.frame

	def stream(self, save_data=False):
		while True:
			frame = self.get_frame()
			# if save_data:
			# 	print('SHOULD SAVE DATA HERE')
			yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

	@classmethod
	def _thread(cls):
		with picamera.PiCamera() as camera:
			# camera setup
			camera.resolution = (320, 240)
			camera.hflip = True
			camera.vflip = False

			# let camera warm up
			# camera.start_preview()
			time.sleep(2)

			stream = io.BytesIO()
			for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
				# store frame
				stream.seek(0)
				cls.frame = stream.read()

				# reset stream for next frame
				stream.seek(0)
				stream.truncate()

				# if there hasn't been any clients asking for frames in
				# the last 10 seconds stop the thread
				if time.time() - cls.last_access > 10:
					break
		cls.thread = None