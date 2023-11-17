import cv2
import numpy as np
img = cv2.imread('../skirt_1.jpg')
# cv2.imshow('img', img)

show = np.full((480, 640, 3), 255, np.uint8)
cv2.imshow('show', show)

show[100:300,200:400] = (0,0,0)
cv2.imshow('show_now', show)

while True:
    out_2 = cv2.bitwise_not(show)
    cv2.imshow('out_2', out_2)

    # out = cv2.bitwise_not(img)
    # cv2.imshow('out', out)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
