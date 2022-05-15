from libs import person_detector, photo_taker,routes_dao

if __name__ == "__main__":
    photo_taker.take_photo("H21")
    person_detector.detect_persons("H21")
