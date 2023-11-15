import cv2
import numpy as np

img = np.zeros((400,700,3), np.uint8)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break
cv2.destroyAllWindows()