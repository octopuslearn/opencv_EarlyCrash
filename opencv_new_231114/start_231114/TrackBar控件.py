# #trackbar-跟踪栏
#
#
# import cv2
# import numpy as np
#
# cv2.namedWindow('show', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('show', width=640, height=480)
#
# #背景
# ##行个数，列个数
# img = np.zeros((480, 640, 3), np.uint8)
#
# def trackbar_callback():
#     pass
#
# #创建Trackbar-跟踪栏 参1-跟踪栏名，参2-窗口名，参3-初始值，参4-最大值，参5-回调函数，参6-回调函数默认数值
# cv2.createTrackbar('b', 'show', 0, 255, trackbar_callback)
# cv2.createTrackbar('g', 'show', 0, 255, trackbar_callback)
# cv2.createTrackbar('r', 'show', 0, 255, trackbar_callback)
#
#
# while True:
#     # cv2.imshow('show', img)
#     #获取trackbar值，参1-trackbar名；参2-trackbar所在的窗口
#     b = cv2.getTrackbarPos('b', 'show')
#     g = cv2.getTrackbarPos('g', 'show')
#     r = cv2.getTrackbarPos('r', 'show')
#     img[:] = [b, g, r]
#     cv2.imshow('show', img)
#     key = cv2.waitKey(1)
#     if key & 0xff == ord('q'):
#         break
#
# cv2.destroyAllWindows()



#trackbar-跟踪栏

import cv2
import numpy as np

cv2.namedWindow('show', cv2.WINDOW_NORMAL)
cv2.resizeWindow('show', width=640, height=480)
cv2.namedWindow('show_1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('show_1', width=480, height=640)

#背景
##行个数，列个数
img = np.zeros((480, 640, 3), np.uint8)
img_1 = np.zeros((640, 480, 3), np.uint8)

def trackbar_callback():
    pass

#创建Trackbar-跟踪栏 参1-跟踪栏名，参2-窗口名，参3-初始值，参4-最大值，参5-回调函数，参6-回调函数默认数值
cv2.createTrackbar('b', 'show', 0, 255, trackbar_callback)
cv2.createTrackbar('g', 'show_1', 0, 255, trackbar_callback)
cv2.createTrackbar('r', 'show_1', 0, 255, trackbar_callback)


while True:
    # cv2.imshow('show', img)
    #获取trackbar值，参1-trackbar名；参2-trackbar所在的窗口
    b = cv2.getTrackbarPos('b', 'show')
    g = cv2.getTrackbarPos('g', 'show_1')
    r = cv2.getTrackbarPos('r', 'show_1')
    img[:] = [b, 0, 0]
    img_1[:] = [0, g, r]
    cv2.imshow('show', img)
    cv2.imshow('show_1', img_1)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()


