import RPi.GPIO as GPIO
from api import api


if __name__ == "__main__":
	api.run(debug=True, host='0.0.0.0')
