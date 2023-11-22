import cv2
import numpy as np



"""
黑底上有白色的噪点- 使用开运算（先腐蚀，再膨胀） 腐蚀去掉了白色的噪点，膨胀恢复原样
"""
img = cv2.imread('kai.png')
cv2.imshow('img', img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8,8))   #调整核的大小即可
out = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('out', out)


"""
白字上有黑点 闭运算（先膨胀，再腐蚀） 膨胀去掉了黑点，腐蚀恢复原样
"""
img = cv2.imread('dotinj.png')
cv2.imshow('img', img)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8,8))
out = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('out', out)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()