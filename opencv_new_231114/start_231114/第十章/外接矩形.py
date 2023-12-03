import cv2
import numpy as np
# 导入图片
img = cv2.imread('hello.jpeg')

#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
#二值化
ret,threshold = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
# cv2.imshow('threshold',threshold)
#查找轮廓
imge, controus, tree = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#最小外接矩形
r = cv2.minAreaRect(controus[1])
box = cv2.boxPoints(r)    #拿到了起始点宽高
box = np.int0(box)  #box是浮点型的，需要强转
cv2.drawContours(img, [box],0,(0,0,255),2)  #因为box是个数组所以[box]

#最大外接矩形
x,y,w,h = cv2.boundingRect(controus[1])
print(x,y,w,h )
cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)


cv2.imshow('img',img)
while True:
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()