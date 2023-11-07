import cv2 #opencv读取格式是BGR
import matplotlib.pyplot as plt
import numpy as np
#魔法指令
# %matplotlib inline
#读取一张图片,指定路径
img = cv2.imread('cat.jpg')

#此处写了个函数替代上面的
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
img
cv_show('cat','cat.jpg')