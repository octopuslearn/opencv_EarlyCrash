import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('video')
while True:
    ret, frame = cap.read()

    cv2.imshow('video', frame)
    key = cv2.waitKey(1000//24)
    if (key & 0xff == ord('q')):
        break
cap.release()
cv2.destroyWindow()
