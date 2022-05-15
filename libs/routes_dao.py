import threading
import platform
import json
from libs import person_detector

paths = {
    "Windows": "C:/SIAM-Data/routes-data.json",
    "Linux": "~/SIAM/routes-data.json",
    "Darwin": "~/SIAM/routes-data.json"
}

data_file_path = paths[platform.system()]


def generate_data_file(route_name=""):
    threading.Timer(30, generate_data_file, [route_name]).start()
    data_on_json = json.dumps({
        "name": route_name,
        "numberOfUsers": person_detector.detect_persons(route_name)
    })
    route_data_file = open(data_file_path, "w")
    route_data_file.write(data_on_json)
