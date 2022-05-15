import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.polynomial import poly


def detect_persons(route_name=""):
    img = cv2.imread("images/{}.jpg".format(route_name))
    box, labels, count = cv.detect_common_objects(img, confidence=0)
    output_image = draw_bbox(img, box, labels, count)
    plt.figure(figsize=(10, 10))
    plt.axis = "off"
    plt.imshow(output_image)
    plt.show()
    person_label_list = list(filter(lambda label: label == "person", labels))
    return len(person_label_list)
