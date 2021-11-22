"""
File: my_drawing.py
Name: Hank周柏翰
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GPolygon,GLine
from campy.graphics.gwindow import GWindow

SIZE = 300       # Controls the size of the pokemon ball and the talking room
WIDTH = (SIZE*8)/3      # Controls the width of the window
HEIGHT = (SIZE*5)/3     # Controls the height of the window


def main():
    """
    1. I will draw a pokemon ball( You can control the size in the global variable 'SIZE' with desired)
    2. Let's catch Jerry!
    """
    window = GWindow(width=WIDTH, height=HEIGHT, title='Pokemon Ball')
    ball = GOval(SIZE, SIZE, x=(window.width-SIZE)/2, y=(window.height-SIZE)/2)
    ball.filled = True
    ball.color = 'red'
    ball.fill_color = 'red'
    window.add(ball)
    # Start to draw the white part
    arc1 = GArc(SIZE*2, SIZE*2, 180, 90, x=(window.width-SIZE)/2, y=(window.height-SIZE)/2)
    arc1.filled = True
    arc1.color = 'white'
    arc1.fill_color = 'white'
    window.add(arc1)
    arc2 = GArc(SIZE*2, SIZE*2, 270, 90, x=(window.width - SIZE) / 2, y=(window.height - SIZE) / 2)
    arc2.filled = True
    arc2.color = 'white'
    arc2.fill_color = 'white'
    window.add(arc2)
    # Line in the middle
    line = GRect(SIZE, SIZE/10, x=(window.width - SIZE) / 2, y=(window.height - SIZE/10) / 2)
    line.filled = True
    window.add(line)
    # black ball in the middle
    circle1 = GOval(SIZE/2.8, SIZE/2.8, x=(window.width-(SIZE/2.8))/2, y=(window.height-(SIZE/2.8))/2)
    circle1.filled = True
    window.add(circle1)
    # white ball in the middle
    circle2 = GOval(SIZE/4, SIZE/4, x=(window.width - (SIZE/4)) / 2, y=(window.height - (SIZE/4)) / 2)
    circle2.filled = True
    circle2.fill_color = 'white'
    window.add(circle2)
    # black circle in the middle
    circle3 = GOval(SIZE/7, SIZE/7, x=(window.width - (SIZE/7)) / 2, y=(window.height - (SIZE/7)) / 2)
    circle3.color = 'black'
    window.add(circle3)
    # triangle of the talking room
    triangle = GPolygon()
    triangle.add_vertex((SIZE*0.71666667, SIZE*0.55))
    triangle.add_vertex((SIZE*0.78333333, SIZE/2))
    triangle.add_vertex((SIZE*0.83333333, SIZE*0.66666667))
    triangle.filled = True
    triangle.color = 'black'
    triangle.fill_color = 'blue'
    window.add(triangle)
    # talking room
    room = GOval(SIZE*0.833333, SIZE*0.5833333, x=SIZE/30, y=SIZE/30)
    room.filled = True
    room.fill_color = 'blue'
    window.add(room)
    # Label in the room
    label = GLabel('Let\'s catch Jerry!', x=SIZE/10, y=SIZE/3)
    label.font = str(-int(SIZE*0.08333333))
    label.color = 'white'
    window.add(label)










if __name__ == '__main__':
    main()
