"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: The filepath that we want to deal with.
    :return: we will return the picture that has been dealt(b_img).
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)  # Make a blank canvas
    for x in range(img.width):
        for y in range(img.height):
            # 舊影像有顏色的
            img_p = img.get_pixel(x, y)
            # 新影像空白1
            b_p1 = b_img.get_pixel(x, y)
            # 新影像空白2
            b_p2 = b_img.get_pixel(x, 2*img.height-y-3)
            # 上色1
            b_p1.red = img_p.red
            b_p1.green = img_p.green
            b_p1.blue = img_p.blue
            # 上色2
            b_p2.red = img_p.red
            b_p2.green = img_p.green
            b_p2.blue = img_p.blue
    return b_img


def main():
    """
    1. We will show you the original picture as original_mt
    2. After we deal the picture with function reflect(), we will show you the reflected picture.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
7777777