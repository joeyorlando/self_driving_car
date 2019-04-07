bind = "0.0.0.0:5001"
workers = 1
threads = 10
# worker_class="gevent" NOTE: to use async worker framework need to make some changes to Camera class code... https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited
preload = True
accesslog = "-"
loglevel = "debug"
proc_name = "web_api"
access_log_format = "%(h)s %(l)s %(u)s %(t)s .%(r)s. %(s)s %(b)s .%(f)s. .%(a)s. host=\"%({Host}i)s\""
