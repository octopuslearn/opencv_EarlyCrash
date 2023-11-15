import cv2
import numpy as np


cv2.namedWindow('show', cv2.WINDOW_NORMAL)
cv2.resizeWindow('show', width=720, height=480)

img = cv2.imread('../cat_1.jpg')


def trackbar_callback():
    pass

colorspaces = [cv2.COLOR_RGB2BGR, cv2.COLOR_RGB2HSV,
               cv2.COLOR_RGB2HLS, cv2.COLOR_RGB2YUV,
               ]
#TrackBar控件
cv2.createTrackbar('color', 'show', 0, 3, trackbar_callback)



while True:
    cv2.imshow('yuan', img)

    index = cv2.getTrackbarPos('color', 'show')
    cvt_img = cv2.cvtColor(img, colorspaces[index])

    cv2.imshow('show', cvt_img)

    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break


cv2.destroyAllWindows()