import cv2
import numpy as np

img = np.zeros((400,700,3), np.uint8)

while True:
    cv2.imshow('img', img)
    # 点
    # img[100, 200] = 255 #100行 100列的这个点 白色
    # img[100, 200, 1] = 255  #g层 100行 200列这个点绿色
    # img[100, 200]= [0,255,0]    #同上
    count = 0
    while count < 200:
        # 线
        # img[100, 0:count] = [255,0,0]
        # img[0:count, 100] = [0, 255, 0]

        # 片
        # img[:, 0:count] = [0, 0, 255]
        # img[0:count, :] = [255, 255, 0]
        # img[:] = [255, 255, 255]

        count += 1
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break
cv2.destroyAllWindows()