
#! template matching
import numpy as np
import cv2

# loading in grayscale
img = cv2.imread("./assets/scene.jpg", 0)
temp = cv2.imread("./assets/grass2.jpg", 0)

h, w = temp.shape
print(img)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
count = 0
for method in methods:
    count+=1
    img2 = img.copy()
    result = cv2.matchTemplate(img2, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    b_location = (location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, b_location, 255, 5)
    img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow(f"Method {count}", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
