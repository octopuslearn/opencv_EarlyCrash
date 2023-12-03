import cv2
import numpy as np

w_min = 100
h_min = 100

cars = []

line_high = 500
offset = 50

carno = 0

def center(x,y,w,h):
    x1 = int(w/2)
    y1 = int(h/2)

    cx = x+x1
    cy = x+y1
    return cx,cy

cap = cv2.VideoCapture('video.mp4')

#一种去背景方法，简单来说是一定时间内不动的为背景，动的是前景。一般不用改，倘若要改只需改history
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()
"""
bgsubmog_1 = cv2.bgsegm.createBackgroundSubtractorMOG()
"""

while True:
    ret,frame = cap.read()
    ###错的while ret:
    if ret:

        # 1.灰度
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # print(gray.shape)
        """       
        mask_1 = bgsubmog_1.apply(gray) #倘若不去噪，去除背景后会有很多的噪点，去点后会好一点
        cv2.imshow('mask_1', mask_1)
        """
        # 2.去噪（去噪前要先灰度）
        bul = cv2.GaussianBlur(gray, (3,3),5)

        # 3.去背景（去背景前线去噪）
        mask = bgsubmog.apply(bul)
        # cv2.imshow('mask', mask)

        #4.腐蚀 去掉图中小的噪点
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        erode = cv2.erode(mask, kernel)

        #5.膨胀 还原 iterations=3指膨胀了3次
        dilate = cv2.dilate(erode ,kernel, iterations=3)

        #6.闭操作 去掉物体内部的小块
        kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
        close = cv2.morphologyEx(dilate, cv2.MORPH_RECT,kernel_1)
        close = cv2.morphologyEx(close, cv2.MORPH_RECT, kernel_1)

        #7.查找轮廓
        image,contours,tree = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        """
            #自己写的法1
            for (i,c) in enumerate(contours):
            area = cv2.contourArea(c)
            if(area > 2500):
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                
            #自己写的法2，和法1相同 
            for (i,c) in enumerate(contours):
            area = cv2.contourArea(c)
            if (area <= 2500):
                continueq
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        """

        # 8.检测线
        cv2.line(frame, (0, line_high), (1280, line_high), (255, 0, 0), 3)


        for (i, c) in enumerate(contours):
            x,y,w,h = cv2.boundingRect(c)

            #验证车辆有效性
            isRight = w<w_min and h<h_min
            if isRight:
                continue
            # 到这里是有效的车 (车的长宽达标)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cpoint = center(x, y, w, h) #获得车中心
            cars.append(cpoint) #将车中心存到cars列表中
            cv2.circle(frame, (cpoint), 5, (0, 0, 255), -1) #车中心画点

            for (x, y) in cars:
                if((y>line_high-offset) and (y<line_high+offset)):
                    carno += 1
                    cars.remove((x,y))
                    print(carno)








        cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()