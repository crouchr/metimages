# POC
# take a picture of the sky so that the picture can be:
# a) send in Forecast Tweet
# b) analysed to determin approximate light level
# c) analysed for cloud coverage

import cv2
import time

cam = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    img_name = "../images/metminiwx_sky_image_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written to disk".format(img_name))
    img_counter += 1

    mins = 10           #10 mins between images
    sleep_secs = mins * 60
    print(time.ctime() + ' sleeping...')
    time.sleep(sleep_secs)

cam.release()



