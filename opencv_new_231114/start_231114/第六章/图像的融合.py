import cv2
import numpy as np
img = cv2.imread('../cat_1.jpg')
img_2 = cv2.imread('../cat_2.jpg')
print(img.shape, img_2.shape)
###注意：只有相同的图才能融合
# 参1-图片a,参2-图片a权重，参3-图片b,参4-图片4的权重，参4-静态的权重（将所有的图片都加上参4）
out = cv2.addWeighted(img, 0.5, img_2, 0.3, 0)
cv2.imshow('out', out)
cv2.waitKey()