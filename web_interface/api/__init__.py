import os
from flask import Flask

web_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../web'))
template_folder = "%s/templates" % web_folder
static_folder = "%s/static" % web_folder

api = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

from api.controllers import *
