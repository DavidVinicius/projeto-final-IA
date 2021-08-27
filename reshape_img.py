import matplotlib.pyplot as plt

img = plt.imread('9.png')
rows, cols, colors = img.shape  # gives dimensions for RGB array
img_size = rows*cols*colors
img_1D_vector = img.reshape(img_size)
print(img_1D_vector.shape)
# you can recover the orginal image with:
img2 = img_1D_vector.reshape(rows, cols, colors)