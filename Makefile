pip-install:
	pip install --no-cache-dir -r requirements.txt
	pip install --no-cache-dir -r requirements-pi.txt

run-web-server:
	gunicorn -c config/gunicorn.py web_interface.api:api --reload