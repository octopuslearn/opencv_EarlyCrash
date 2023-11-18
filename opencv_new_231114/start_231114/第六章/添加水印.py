#方法：
# 1.导入图，Logo
# 2.获得logo掩膜
# 3.将要添加Logo的图的位置，变成黑色
# 4.将Logo与要添加logo的位置的图相加
# 5.将4赋值给要添加水印的图
import cv2
import numpy as np

skirt = cv2.imread('../skirt_1.jpg')
# print(skirt.shape)
#创建logo
img = np.zeros((200, 200, 3), np.uint8) #logo
img[0:100,0:100] = [255, 0, 0]
img[50:150,50:150] = [0, 255, 0]


#为了在skirt中加水印（与操作），需要Logo为黑背景为白的图片，而logo所在的图片是背景为黑的，所以先绘制背景为黑logo处为白的图
mak = np.zeros((200, 200), np.uint8)
mak[0:100,0:100] = 255
mak[50:150,50:150] = 255

# 掩膜
#对背景为黑logo处为白的图取反，获得背景为白logo为黑的图
mak_2 = cv2.bitwise_not(mak)

roi = skirt[0:200, 0:200]
#按位与用于掩膜操作，两幅图片对应的像素通过按位与。用于图像的特定区域与另一图像合并或者提取
##参1,2-输入图片；参3-掩模图像，制定了那些像素进行按位与操作。如果None则表示所有像素进行操作
###如果前两个参数相同，效果是对roi中的每个像素都应用掩膜。用于过滤或者提取感兴趣的区域，将某些像素置零或者保留
####mak_2会对roi每个通道进行按位与运算（图像中的按位与是对像素进行的，对于像素而言非0即为真即1）
mak_3 = cv2.bitwise_and(roi, roi, mask=mak_2)

mak_4 = cv2.add(mak_3,img)

skirt[0:200,0:200] = mak_4


while True:

    # cv2.imshow('skirt', skirt)
    # cv2.imshow('img' ,img)
    # cv2.imshow('mak', mak)
    # cv2.imshow('mak_2',mak_2)
    cv2.imshow('mak_3', mak_3)
    cv2.imshow('mak_4', mak_4)
    cv2.imshow('skirt', skirt)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()







