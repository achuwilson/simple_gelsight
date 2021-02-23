from get_image import imageReader
import cv2
import time
#getImage()

c0=imageReader('http://raspberrypi.local:8088/stream')



while True:
    im0 = c0.getFrame()

    cv2.imshow("IMAGE0",im0)

    cv2.waitKey(1)  
