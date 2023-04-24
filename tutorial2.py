import cv2
import random

img = cv2.imread("./assets/img.jpg", -1)

#! an image is stored in a numpy array as a multi-dimensional array of pixel values. Each pixel value represents the intensity of the color channel(s) at that particular location in the image.

# a grayscale image is stored as a 2D numpy array with each element representing the intensity of a single pixel. A color image

# A color image, on the other hand, is stored as a 3D numpy array where each element represents the intensity of a single pixel for each color channel (red, green, blue).

# ? The shape of the numpy array represents the dimensions of the image. For example, a grayscale image of size 512x512 would be stored as a numpy array of shape (512, 512), whereas a color image of size 512x512 would be stored as a numpy array of shape (512, 512, 3).

# print(img)          # ! (height,width,(r,g,b))
# print(type(img))
# print(img[0][0])    # ! (blue,green,red)


# #! changing pixel value
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(
#             0, 255), random.randint(0, 255)]


#!copy ane part of image and paste to same
# ? copying part of array and replacing it to another place

tag = img[50:350, 200:450]  # !500 to 700 rows and 600:900 column

img[350:650, 100:350] = tag

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
