# POC
# take a picture of the sky so that the picture can be:
# a) send in Forecast Tweet
# b) analysed to determine approximate light level
# c) analysed for cloud coverage

import cv2
import time
import twitter

cam = cv2.VideoCapture(0)

while True:
    print('started')
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    img_name = "../images/metminiwx_sky_image_" + time.ctime()  + '.png'
    img_name = img_name.replace('  ', ' ')
    img_name = img_name.replace(' ', '_')
    img_name = img_name.replace(':', '_')
    cv2.imwrite(img_name, frame)
    print("{} written to disk".format(img_name))

    # Tweet the picture
    tweet = 'TESTING : View of sky'
    status = twitter.send_tweet(tweet, hashtags=None, image_pathname=img_name)

    mins = 60                   # 1 hour between images
    sleep_secs = mins * 60
    print(time.ctime() + ' sleeping...')
    time.sleep(sleep_secs)

cam.release()
