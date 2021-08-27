import cv2
import numpy as np

im = cv2.imread("5.png", cv2.IMREAD_GRAYSCALE)
print(im.shape)
im = cv2.resized_image = cv2.resize(im, (28, 28))
im = cv2.bitwise_not(im)
#print(im.shape)

thresh = 127
#im_bw = cv2.threshold(im, thresh, 255, cv2.THRESH_BINARY)[1]
im_bw = im
cv2.imwrite('bw_image.png', im_bw)

height, width = im.shape[:2]
img = im
max_height = 28
max_width = 28

# only shrink if img is bigger than required
if max_height < height or max_width < width:
    # get scaling factor
    scaling_factor = max_height / float(height)
    if max_width/float(width) < scaling_factor:
        scaling_factor = max_width / float(width)
    # resize image
    img = cv2.resize(img, None, fx=scaling_factor,
                     fy=scaling_factor, interpolation=cv2.INTER_AREA)

img = np.matrix(img)
print(img.getA1())
#cv2.imshow("Shrinked image", img)
