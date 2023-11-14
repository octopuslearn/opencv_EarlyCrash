import cv2
import numpy as np
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', width=480, height=320)
cap = cv2.VideoCapture(1)

#创建VideoWrite为写多媒体文件
"""
以下，教程没有问题
"""
###注意这里必须设置为摄像头的分辨率，否则出错
####opencv看到真实的设定的不同时，不会输出
#####至于编码器(*MJPG)和.mp4(.avi)经过测试都行
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vm = cv2.VideoWriter('./video_mp4_1.avi', fourcc, 25, (640, 480))
"""
以上，教程没有问题
"""

"""
以下，官方教程没有问题
"""
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# vm = cv2.VideoWriter('./video_9.avi', fourcc, 25, (640, 480))
"""
以上，官方教程没有问题
"""
while cap.isOpened():
    tmp, frame = cap.read()
    if tmp == True:
        cv2.imshow('video', frame)
        #写入数据帧
        vm.write(frame)
        key = cv2.waitKey(1)
        if key & 0xff == ord('q'):
            break
    else:
        print("摄像头打开失败！")
        break
#释放VideoCapture
cap.release()
#释放VideoWrite
vm.release()
cv2.destroyWindos()