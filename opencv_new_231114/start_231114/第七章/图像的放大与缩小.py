import cv2
import numpy as np

skirt = cv2.imread('../skirt_1.jpg')
print(skirt.shape)


while True:

    cv2.imshow('skirt', skirt)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
