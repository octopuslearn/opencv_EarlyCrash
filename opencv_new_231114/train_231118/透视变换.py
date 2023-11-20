import cv2
import numpy as np


cat_1 = cv2.imread('./chun_long.jpg')
print(cat_1.shape)
cat_2 = cv2.imread('./banai.jpg')
print(cat_2.shape)
cat_1 = cv2.resize(cat_1, None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
cat_2 = cv2.resize(cat_2, None,fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR)
print(cat_1.shape)

h,w,ch = cat_2.shape
h_2,w_2,ch_2 = cat_1.shape

#透视变换是3*3的矩阵

src = np.float32([[0,0],[100,300],[100,700],[0,700]])
dst = np.float32([[0,0],[512,0],[512,768],[0,768]])
M = cv2.getPerspectiveTransform(src,dst)
cat_out_1_1 = cv2.warpPerspective(cat_1, M, (w,h))
cv2.imshow('cat_out_1_1',cat_out_1_1)
cv2.imshow('cat_1',cat_1)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()