from PIL import Image

from resizeimage import resizeimage

size = 8, 8

im = Image.open("9-2.png").convert("L")
im.thumbnail((8, 8), Image.ANTIALIAS)
im.save("9-222.png", "JPEG")
