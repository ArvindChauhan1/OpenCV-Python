
#! detecting corner

import numpy as np
import cv2

img = cv2.imread("./assets/chess.jpg")
img = cv2.resize(img, (0, 0), fx=1, fy=1)

# ? converting to grayscale (easier to detect)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ? corners= cv2.goodFeaturesToTrack(source,number of corners,minimum quality of corners (o to 1),MINIMUM EUCLIDEAN DISTANCE)

# ? two points in a two-dimensional space (x1,y1) and (x2,y2)
# ? d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# ? converting to integer
corners = np.int0(corners)
# print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 12, (255, 0, 0), 2)

for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
