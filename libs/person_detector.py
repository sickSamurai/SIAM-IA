import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
import threading
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly


def detect_persons(route_name=""):
    img = cv2.imread("images/{}.jpg".format(route_name))
    box, labels, count = cv.detect_common_objects(img, confidence=0)
    person_label_list = list(filter(lambda label: label == "person", labels))
    return len(person_label_list)


def generate_data_file(route_name=""):
    threading.Timer(30, generate_data_file, [route_name]).start()
    data_on_json = json.dumps({
        "name": route_name,
        "numberOfUsers": detect_persons(route_name)
    })
    route_data_file = open("C:/SIAM-Data/routes-data.json", "w")
    route_data_file.write(data_on_json)
