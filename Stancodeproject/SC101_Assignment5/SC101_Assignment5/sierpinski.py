"""
File: sierpinski.py
Name: Hank 周柏翰
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6              # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	We are going to draw a fractal called 'Sierpinski Triangle'.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The order of Sierpinski Triangle.
	:param length: The length  of order 1 Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle
	:return: we will print out the Sierpinski Triangle
	"""
	if order == 0:
		pass
	else:
		# Middle Triangle
		x1 = upper_left_x
		y1 = upper_left_y
		x2 = upper_left_x + length
		y2 = upper_left_y
		x3 = upper_left_x + length*0.5
		y3 = upper_left_y + length*0.866
		l1 = GLine(x1, y1, x2, y2)
		l2 = GLine(x1, y1, x3, y3)
		l3 = GLine(x2, y2, x3, y3)
		window.add(l1)
		window.add(l2)
		window.add(l3)
		# Left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# Lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+(length*0.866/2))






if __name__ == '__main__':
	main()