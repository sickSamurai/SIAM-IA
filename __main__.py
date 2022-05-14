from libs import person_detector, photo_taker

if __name__ == "__main__":
    photo_taker.take_photo("H21")
    person_detector.generate_data_file("H21")
