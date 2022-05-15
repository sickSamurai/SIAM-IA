import os.path
import threading
import json

from libs.person_detector import *

data_file_path = os.path.expanduser("~/SIAM")


def generate_data_file(route_name=""):
    data_on_json = json.dumps({
        "name": route_name,
        "numberOfUsers": detect_persons(route_name)
    })
    if not os.path.exists(data_file_path):
        os.mkdir(data_file_path)
    route_data_file = open("{}/routes-data.json".format(data_file_path), "w")
    route_data_file.write(data_on_json)
