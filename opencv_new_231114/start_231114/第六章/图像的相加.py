import cv2
import numpy as np

#加法运算是矩阵的运算 所以图片的尺寸要相同
img = cv2.imread('../skirt_1.jpg')
img_2 = np.ones((604, 403, 3), np.uint8)*2
print(img.shape)
print(img_2.shape)
while True:
    cv2.imshow('img', img)
    cv2.imshow('img_2', img_2)
    # #图像的加法
    # img_out = cv2.add(img, img_2)
    # cv2.imshow('img_out', img_out)
    #
    # #减法 参1-被减数，参2-减数
    # #图像的减法 减法并不会回到原来的 为什么我的差别如此之大
    # img_out_2 = cv2.subtract(img_out, img_2)
    # cv2.imshow('img_out_2', img_out_2)
    #
    # img_out_3 = cv2.subtract(img, img_2)
    # cv2.imshow('img_out_3', img_out_3)

    # 乘法 让图片亮的更快
    out_1 = cv2.multiply(img, img_2)
    cv2.imshow('out_1', out_1)

    # 除法 让图片暗的更快
    out_2 = cv2.divide(out_1, img_2)
    cv2.imshow('out_2', out_2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()