import cv2

# loading image
img = cv2.imread('./assets/img.jpg', 1)

# ? cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.

# ? cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.

# ? cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.


# resize the image and rotate
# img = cv2.resize(img, (700, 400))       # width the height

# modifying orignal image pixed by x and y axis
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("./assets/new_img.jpg", img)


cv2.imshow("image", img)  # show image

cv2.waitKey(0)  # wait infinite time until key pressed
# cv2.waitKey(5)  # wait 5 sec time until key pressed

cv2.destroyAllWindows()
