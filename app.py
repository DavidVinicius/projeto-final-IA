import cv2
import numpy as np
import pickle

with open('model/mlp_model.pkl', 'rb') as fid:
    model = pickle.load(fid)

im = cv2.imread("5.png", cv2.IMREAD_GRAYSCALE)
print(im.shape)
im = cv2.resized_image = cv2.resize(im, (28, 28))
#print(im.shape)

thresh = 127
im_bw = cv2.threshold(im, thresh, 255, cv2.THRESH_BINARY_INV)[1]
#im_bw = im
cv2.imwrite('bw_image.png', im_bw)

img = np.matrix(im_bw).getA1()
print(img)
#cv2.imshow("Shrinked image", img)

I = np.array([img])

classe = model.predict(I)
print("Classe Predita: {}".format(str(classe)))
