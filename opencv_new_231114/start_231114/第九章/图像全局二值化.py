import cv2
import numpy as np

skirt = cv2.imread('../cat_1.jpg')
skirt_gray = cv2.cvtColor(skirt,cv2.COLOR_BGR2GRAY)
cv2.imshow('skirt_gray', skirt_gray)

#全局二值化
#参2-阈值 参3-当像素超过阈值时设置的值，通常为255
#参4-type阈值处处理类型：cv2.THRESH_BINARY-大于阈值的部分设置为maxval,小于的设置为0
#####################cv2.THRESH_BINARY_INV-大于阈值的部分设置为0，小于的部分设置为maxval

#返回值 retval-实际阈值 threshold_image-经阈值处理后的图像，显示为二值图像
retval,skirt_threshold = cv2.threshold(skirt_gray, 100, 255, type=cv2.THRESH_BINARY)
retval_1,skirt_threshold_1 = cv2.threshold(skirt_gray, 100, 255, type=cv2.THRESH_BINARY_INV)
print(retval_1) #100
cv2.imshow('skirt_threshold', skirt_threshold)
cv2.imshow('skirt_threshold_1', skirt_threshold_1)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()