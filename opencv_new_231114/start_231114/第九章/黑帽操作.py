import cv2
import numpy as np

img = cv2.imread('./heimao.png')
cv2.imshow('img', img)
# 卷积核必须足够大，因为噪点很大
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
out = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('out', out)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()