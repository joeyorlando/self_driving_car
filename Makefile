pip-install:
	pip install -r requirements.txt
	pip install -r requirements-pi.txt

run-web-server:
	gunicorn -c config/gunicorn.py web_interface.api:api --reload