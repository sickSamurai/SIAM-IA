import os

import cv2
import threading


def take_photo(route_name=""):
    # configure for take photos periodically
    threading.Timer(30, take_photo, [route_name]).start()
    # initialize the camera
    cam = cv2.VideoCapture(0)  # 0 -> index of camera
    result, image = cam.read()
    if result:
        current_directory = os.getcwd()
        cv2.imwrite("{}/images/{}.jpg".format(current_directory, route_name), image)
