import cv2

cv2.namedWindow('video')
cv2.resizeWindow('video', 640, 360)

#获取视频设备
cap = cv2.VideoCapture(0)

#判断摄像头是否打开
while cap.isOpened():
    while True:
        #从摄像头读取视频帧
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('video', frame)
            key = cv2.waitKey(1000//24)
            if (key & 0xff == ord('q')):
                break
else:
    print("摄像头打开失败")
    break

 #释放VideoCapture
cap.release()
cv2.destroyWindow()
