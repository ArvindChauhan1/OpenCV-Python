import numpy as np
import cv2

#!If you have.Multiple cameras, then 0 will access the primary 1 will access the secondary, 2 will access the ternary, so on.
#! video file can also be used
cap = cv2.VideoCapture(0)

#! displaying video
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # ! start and ending cordinate, topleft is (0,0)
    # ? width and height points to bottom
    # ? cv2.line(image, start_point, end_point, color, thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (width, 0), (0, height), (0, 0, 255), 5)

    #! cv2.rectangle(image, start_point, end_point, color, thickness)
    # ? for a solid rectangle, set the thickness parameter to a negative value or use the constant cv2.FILLED
    img = cv2.rectangle(img, (100, 100), (200, 200), (45, 85, 4), 5)

    #! cv2.circle(image, center, radius, color, thickness)
    # ? for a solid (filled) circle, thickness parameter = negative value or cv2.FILLED.
    img = cv2.circle(img, (width//2, height//2), 200, (0, 10, 128), 8)

    #! Choose the font and its properties:
    font = cv2.FONT_HERSHEY_SIMPLEX

    #! cv2.putText(img, text, org, font, fontScale, color, thickness, lineType(optional))
    # ? org: is the coordinates of the bottom-left corner of the text string in the image.
    # ? fontScale: is the font scale factor that is multiplied by the font-specific base size.
    # ? lineType: is the type of line used to draw the text string (e.g., cv2.LINE_AA for anti-aliased line).
    img = cv2.putText(img, "Arvind is Great", (100, height-10),
                      font, 1, (256, 256, 256,), 2)

    cv2.imshow('frame', img)

    # ? gonna wait 1 milisecond for input key, if key == q loop will break and the imshow will stop
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
