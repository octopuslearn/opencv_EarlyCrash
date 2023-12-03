import cv2
import numpy as np
# 导入图片
img = cv2.imread('tubao_bijin.png')

# 转为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

#二值化
ret,threshold = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

###错误 由于这里和img = cv2.imread('tubao_bijin.png')名字一致所以画不出来轮廓
# img,contours,tree = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 找轮廓
imge,contours,tree = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


def drawShape(src, points):
    i=0
    while i < len(points):  #当是最后一个点时，连接到起始点（封闭）
        if(i==len(points)-1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),3)
            # i = i + 1###是这里错了 使得一直是i=31成了死循环，调试看出来的！！！
        i = i + 1
#多边形逼近 参1-轮廓，参2-逼近精度（越小越逼近），参3-是否是封闭轮廓，一般是True
e = 5
approxPolyDP = cv2.approxPolyDP(contours[0], e, True)
approxPolyDP = cv2.approxPolyDP(contours[0], e, False)  #看起来好像没啥影响
drawShape(img,approxPolyDP)



# 凸包 参1-轮廓
hull = cv2.convexHull(contours[0])
drawShape(img,hull)

cv2.imshow('img',img)
while True:
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()