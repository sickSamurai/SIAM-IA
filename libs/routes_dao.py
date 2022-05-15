import os.path
import threading
import platform
import json
from libs import person_detector

paths = {
    "Windows": "C:/SIAM-Data",
    "Linux": "~/SIAM",
    "Darwin": "~/SIAM"
}

data_file_path = paths[platform.system()]


def generate_data_file(route_name=""):
    threading.Timer(30, generate_data_file, [route_name]).start()
    data_on_json = json.dumps({
        "name": route_name,
        "numberOfUsers": person_detector.detect_persons(route_name)
    })
    if not os.path.exists(data_file_path):
        os.mkdir(data_file_path)
    route_data_file = open("{}/routes-data.json".format(data_file_path), "w")
    route_data_file.write(data_on_json)
