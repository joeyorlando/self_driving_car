import os
import yaml

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/config.yaml')), "r") as f:
  config = yaml.load(f)
