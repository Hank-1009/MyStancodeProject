"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: The path of  the picture that we want to shrink. 
    :return img: b_img, the shrinkage image.
    """
    img = SimpleImage("images/poppy.png")
    b_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(img.width):
        for y in range(img.height):
            a = img.get_pixel(x, y)
            b = b_img.get_pixel(x//2, y//2)
            b.red = a.red
            b.green = a.green
            b.blue = a.blue
    return b_img


def main():
    """
    1. 1. We will show you the original picture as original
    2. After we deal the picture with function shrink(), we will show you the shrink to 1/2 picture as after_shrink.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
