import cv2
import numpy as np
dian = cv2.imread('./diansai_small.jpg')
dian = cv2.resize(dian,None,fx=0.5,fy=0.5)
cv2.imshow('dian', dian)
skirt = cv2.imread('../cat_1.jpg')
#100以下不是边缘，200以上是边缘
dian_Canny = cv2.Canny(dian,100, 200)
cv2.imshow('dian_Canny', dian_Canny)
# skirt_Canny = cv2.Canny(skirt,150, 180)
# cv2.imshow('skirt_Canny', skirt_Canny)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()