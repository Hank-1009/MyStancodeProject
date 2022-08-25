"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The image that we want to blur
    :return: Image after one time of blurring
    """
    w = img.width  # image's width = w
    h = img.height  # image's height = h
    new_img = SimpleImage.blank(w, h)  # make a new image
    for x in range(img.width):
        for y in range(img.height):
            if x == 0 and y == 0:  # (0,0) case
                pixel_1 = img.get_pixel(x+1, y)
                pixel_2 = img.get_pixel(x, y+1)
                pixel_3 = img.get_pixel(x+1, y+1)
                pixel = img.get_pixel(0, 0)
                new_red = (pixel_1.red+pixel_2.red+pixel_3.red+pixel.red)//4
                new_green = (pixel_1.green+pixel_2.green+pixel_3.green+pixel.green)//4
                new_blue = (pixel_1.blue+pixel_2.blue+pixel_3.blue+pixel.blue)//4
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x == 0 and y == (img.height-1):  # (0,h-1) case
                pixel_1 = img.get_pixel(x+1, y-1)
                pixel_2 = img.get_pixel(x, y-1)
                pixel_3 = img.get_pixel(x+1, y)
                pixel = img.get_pixel(x, y)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel.red) //4
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel.green) //4
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel.blue) //4
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if y == 0 and x == (img.width-1):  # (w-1,0) case
                pixel_1 = img.get_pixel(x-1, y)
                pixel_2 = img.get_pixel(x, y+1)
                pixel_3 = img.get_pixel(x-1, y+1)
                pixel = img.get_pixel(x, y)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel.red) //4
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel.green) //4
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel.blue) //4
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x == (img.width-1) and y == (img.height-1):  # (w-1,h-1) case
                pixel_1 = img.get_pixel(x-1, y)
                pixel_2 = img.get_pixel(x, y-1)
                pixel_3 = img.get_pixel(x-1, y-1)
                pixel = img.get_pixel(x, y)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel.red) //4
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel.green) //4
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel.blue) //4
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x == 0 and y != 0 and y != (img.height-1):  # (0,y) case, y != h-1
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y+1)
                pixel_3 = img.get_pixel(x, y-1)
                pixel_4 = img.get_pixel(x+1, y)
                pixel_5 = img.get_pixel(x+1, y+1)
                pixel_6 = img.get_pixel(x+1, y-1)
                new_red = (pixel_1.red+pixel_2.red+pixel_3.red+pixel_4.red+pixel_5.red+pixel_6.red)//6
                new_green = (pixel_1.green+pixel_2.green+pixel_3.green+pixel_4.green+pixel_5.green+pixel_6.green)//6
                new_blue = (pixel_1.blue+pixel_2.blue+pixel_3.blue+pixel_4.blue+pixel_5.blue+pixel_6.blue)//6
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x != 0 and y == 0 and x != (img.width-1):  # (x,0) case, x != w-1
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y + 1)
                pixel_3 = img.get_pixel(x+1, y)
                pixel_4 = img.get_pixel(x+1, y+1)
                pixel_5 = img.get_pixel(x-1, y)
                pixel_6 = img.get_pixel(x-1, y+1)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red + pixel_6.red)//6
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green + pixel_6.green)//6
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue + pixel_6.blue)//6
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x != 0 and y != 0 and x != img.width-1 and y != img.height-1:  # (x,y) case, and x,y!=0
                new_red = 0
                new_green = 0
                new_blue = 0
                for k in range(-1, 2):  # use for loop to make the process easier, k will be -1,0 and 1
                    pixel_1 = img.get_pixel(x-1, y+k)
                    pixel_2 = img.get_pixel(x+1, y+k)
                    pixel_3 = img.get_pixel(x, y+k)
                    new_red += pixel_1.red + pixel_2.red + pixel_3.red
                    new_green += pixel_1.green + pixel_2.green + pixel_3.green
                    new_blue += pixel_1.blue + pixel_2.blue + pixel_3.blue
                new_red = new_red // 9
                new_green = new_green // 9
                new_blue = new_blue // 9
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if x == (img.width-1) and y != 0 and y != (img.height-1):  # special case of the border when x==w-1
                # y != 0 and y != h-1
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y + 1)
                pixel_3 = img.get_pixel(x, y-1)
                pixel_4 = img.get_pixel(x-1, y)
                pixel_5 = img.get_pixel(x-1, y+1)
                pixel_6 = img.get_pixel(x-1, y-1)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red + pixel_6.red) // 6
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green + pixel_6.green) // 6
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue + pixel_6.blue) // 6
                repeat(new_img, x, y, new_red, new_green, new_blue)
            if y == (img.height-1) and x != 0 and x != (img.width-1):  # special case of the border when y==h-1
                # x != 0 and x != w-1
                pixel_1 = img.get_pixel(x,y)
                pixel_2 = img.get_pixel(x-1, y)
                pixel_3 = img.get_pixel(x+1, y)
                pixel_4 = img.get_pixel(x, y-1)
                pixel_5 = img.get_pixel(x-1, y-1)
                pixel_6 = img.get_pixel(x+1, y-1)
                new_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red + pixel_6.red) // 6
                new_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green + pixel_6.green) // 6
                new_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue + pixel_6.blue) // 6
                repeat(new_img, x, y, new_red, new_green, new_blue)
    return new_img


def repeat(new_img, x, y, new_red, new_green, new_blue):
    """
    :param new_img: The image that we want to blur
    :param x : int, x of the pixel
    :param y : int, y of the pixel
    :param new_red: The average number of the pixel's red part
    :param new_green: The average number of the pixel's green part
    :param new_blue: The average number of the pixel's blue part
    """
    pixel_0 = new_img.get_pixel(x, y)
    pixel_0.red = new_red
    pixel_0.green = new_green
    pixel_0.blue = new_blue


def main():
    """
    1. We will show you the original picture as old_img
    2. After we deal the picture with function blur(), we will show you the blurred picture as blurred_img.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


"""
#It's another solution of the 6 pixel's case
#Just for me to remember

new_red = 0
new_green = 0
new_blue = 0
for i in range(2):  # (x,0) case
    pixel_1 = img.get_pixel(x+1, i)
    pixel_2 = img.get_pixel(x-1, i)
    pixel_3 = img.get_pixel(x, i)
    new_red += pixel_1.red + pixel_2.red + pixel_3.red
    new_green += pixel_1.green + pixel_2.green + pixel_3.green
    new_blue += pixel_1.blue + pixel_2.blue + pixel_3.blue
    new_red = new_red//3
    new_green = new_green//3
    new_blue = new_blue//3
repeat(new_img, x, y, new_red, new_green, new_blue)
"""
if __name__ == '__main__':
    main()
