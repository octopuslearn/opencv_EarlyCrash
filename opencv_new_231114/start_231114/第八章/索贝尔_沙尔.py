import cv2
import numpy as np
skirt = cv2.imread('./chess.png')
dian = cv2.imread('./diansai_small.jpg')
print(dian.shape)
dian = cv2.resize(dian,None,fx=0.5,fy=0.5)
print(dian.shape)
cv2.imshow('skirt',skirt)
cv2.imshow('dian', dian)

#Sobel索贝尔算子
##ksize = -1为沙尔算子。倘若不设默认为3*3
#参1-输入图像，参2-图像深度（数据类型）
#dx,dy分别表示x和y方向上的导数阶数
#ksize-Sobel算子的内核大小，必须是1,3,5或7
#scale-导数结果的缩放因子
#delta-导数结果的偏移值
#borderType-图像边界的处理方式

###x=1,（水平方向）检测出y边  y=1,(垂直方形) 检测出x边
skirt_x = cv2.Sobel(skirt,-1,1,0,ksize=3)
skirt_y = cv2.Sobel(skirt,-1,0,1,ksize=3)
skirt_xy = cv2.add(skirt_x,skirt_y)
cv2.imshow('skirt_x',skirt_x)
cv2.imshow('skirt_y',skirt_y)
cv2.imshow('skirt_xy',skirt_xy)

#
# dian_x = cv2.Sobel(dian,-1,1,0,ksize=3)
# dian_y = cv2.Sobel(dian,-1,0,1,ksize=3)
#ksize=-1 沙尔算子
# dian_x = cv2.Sobel(dian,-1,1,0,ksize=-1)
# dian_y = cv2.Sobel(dian,-1,0,1,ksize=-1)
# dian_xy = cv2.add(dian_x,dian_y)
# cv2.imshow('dian_x', dian_x)
# cv2.imshow('dian_y', dian_y)
# cv2.imshow('dian_xy', dian_xy)

#沙尔算子
##感觉和索贝尔算子ksize=-1时相同
# dian_x = cv2.Scharr(dian,-1,1,0)
# dian_y = cv2.Scharr(dian,-1,0,1)
# dian_xy = cv2.add(dian_x,dian_y)
# cv2.imshow('dian_x', dian_x)
# cv2.imshow('dian_y', dian_y)
# cv2.imshow('dian_xy', dian_xy)



#抗噪能力差 要先去噪
print(dian.shape)
dian_x = cv2.Laplacian(dian,-1,ksize=3)
print(dian_x.shape)
cv2.imshow('dian_x', dian_x)




while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()