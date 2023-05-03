
#! colors and color detection

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#! displaying video
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # ? (src, color code)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([70, 40, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    # cv2.imshow('mask', mask)

    # ?stop code
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


# cv2.cvtColor(frame(pixel here( pixel is converted to image))[[[255,0,0]]], cv2.COLOR_BGR2HSV)
# BGR_Color = np.array([255, 0, 0])
# x = cv2.cvtColor(BGR_Color, cv2.COLOR_BGR2HSV)
# print(x)
