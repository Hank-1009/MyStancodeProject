"""
File: draw_line.py
Name: Hank周柏翰
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# This constant controls the size of the GOval
SIZE = 10

# Global variables:
window = GWindow()
t = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(m):
    global t
    global x1
    global y1
    global x2
    global y2
    global circle1
    t = t+1
    k = 0
    if t % 2 == 1:  # t is odd
        x1 = m.x
        y1 = m.y
        circle1 = GOval(SIZE, SIZE, x=m.x - SIZE/2, y=m.y - SIZE/2)
        circle1.color = 'black'
        window.add(circle1)
    if t % 2 == 0:  # t is even
        x2 = m.x
        y2 = m.y
        k = k+1
    if k == 1:
        line = GLine(x1, y1, x2, y2)
        window.add(line)
        window.remove(circle1)














if __name__ == "__main__":
    main()
