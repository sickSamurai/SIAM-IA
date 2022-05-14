import cv2
import threading


def take_photo(route_name=""):
    # configure for take photos periodically
    threading.Timer(30, take_photo).start()

    # initialize the camera
    cam = cv2.VideoCapture(0)  # 0 -> index of camera
    result, image = cam.read()
    if result:
        cv2.imwrite("images/{}.jpg".format(route_name), image)
        print("Foto tomada con exito")

