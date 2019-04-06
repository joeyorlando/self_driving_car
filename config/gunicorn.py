bind = "0.0.0.0:5001"
workers=2
preload = True
accesslog = "-"
loglevel = "INFO"
proc_name = "web_api"
access_log_format = "%(h)s %(l)s %(u)s %(t)s .%(r)s. %(s)s %(b)s .%(f)s. .%(a)s. host=\"%({Host}i)s\""
