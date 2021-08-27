from PIL import Image

from resizeimage import resizeimage


with open('2.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [8, 8])
        cover.save('xxxx.png', image.format)
