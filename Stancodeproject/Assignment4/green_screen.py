"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: The background image that we want to put in.
    :param figure_img: The figure image with green screen.
    :return: We will return figure image that has been dealt.
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)
            f_pixel = background_img.get_pixel(x, y)
            new_red = f_pixel.red
            new_green = f_pixel.green
            new_blue = f_pixel.blue
            if pixel.green > bigger:
                pixel.red = new_red
                pixel.green = new_green
                pixel.blue = new_blue
    return figure_img


def main():
    """
    1. We will have two original pictures: space_ship and figure(a green screen picture)
    2. Using the combine function, we will combine two picture. (we will use the space_ship background to cover the
    green screen.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
