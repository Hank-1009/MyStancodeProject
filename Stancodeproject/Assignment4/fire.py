"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: The filepath that we want to detect.
    :return: we will return the picture that has been dealt(fire_img).
    """
    fire_img = SimpleImage(filename)
    for pixel in fire_img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > (avg*HURDLE_FACTOR):
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fire_img


def main():
    """
    1. We will show you the original picture as original_fire
    2. After we deal the picture with function highlight_fires(), we will show you the fire area.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
