import cv2
import numpy as np

# 读取图像
image = cv2.imread("yuan_1_3/mask_5.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("yuan", image)
# 定义膨胀核大小和迭代次数
kernel_size = 3
iterations = 1
# 创建膨胀核
kernel = np.ones((kernel_size, kernel_size), np.uint8)
# 定义腐蚀核大小和迭代次数
kernel_size = 3
iterations = 1
# 创建腐蚀核
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# 膨胀操作
image = cv2.dilate(image, kernel, iterations=iterations)

# 腐蚀操作
image = cv2.erode(image, kernel, iterations=iterations)

# # 腐蚀操作
# image = cv2.erode(image, kernel, iterations=iterations)

# # 膨胀操作
# image = cv2.dilate(image, kernel, iterations=iterations)




# 保存输出图像
a = cv2.imwrite('./yuan_1_4/mask_5.png', image)
print(a)
cv2.imshow("out", image)
while True:
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()