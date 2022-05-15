import os.path
import threading
import platform
import json
from libs import person_detector

data_file_path = os.path.expanduser("~/SIAM")


def generate_data_file(route_name=""):
    threading.Timer(15, generate_data_file, [route_name]).start()
    data_on_json = json.dumps({
        "name": route_name,
        "numberOfUsers": person_detector.detect_persons(route_name)
    })
    if not os.path.exists(data_file_path):
        os.mkdir(data_file_path)
    route_data_file = open("{}/routes-data.json".format(data_file_path), "w")
    route_data_file.write(data_on_json)
