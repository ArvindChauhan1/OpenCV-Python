import numpy as np
import cv2

#!If you have.Multiple cameras, then 0 will access the primary 1 will access the secondary, 2 will access the ternary, so on.
#! video file can also be used
cap = cv2.VideoCapture(0)

#! displaying video
while True:
    # ?ret tells capture works or not
    ret, frame = cap.read()  # ? return frame(image) in numpy array
    width = int(cap.get(3))  # ? 3 and 4 are properties of width and height
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)  # ? entire array with zero,

    # resize image
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    #? # rotate
    #? smaller_frame = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top right
    image[height//2:, width//2:] = smaller_frame  # bottom right
    image[height//2:, :width//2] = smaller_frame  # bottom right

    cv2.imshow('frame', image)

    # ? gonna wait 1 milisecond for input key, if key == q loop will break and the imshow will stop
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
