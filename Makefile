pip-install:
	pip install --no-cache-dir -r requirements.txt

run-web-server:
	gunicorn -c config/gunicorn.py web_interface.api:api --reload