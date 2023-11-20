import cv2
import numpy as np
skirt = cv2.imread('./papper.png')
skirt_2 = cv2.imread('./gaussian.png')

#中值滤波 滤除胡椒噪点
#参1-原图，参2-核 ###！！！注意：核是一个数，且是个正奇数
medianBlur_skirt = cv2.medianBlur(skirt, 5)
cv2.imshow('medianBlur_skirt',medianBlur_skirt)

medianBlur_skirt_2 = cv2.medianBlur(skirt, 5)
cv2.imshow('medianBlur_skirt_2',medianBlur_skirt_2)

while True:
    cv2.imshow('skirt',skirt)
    cv2.imshow('skirt_2', skirt_2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()