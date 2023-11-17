import cv2
import numpy as np


while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()