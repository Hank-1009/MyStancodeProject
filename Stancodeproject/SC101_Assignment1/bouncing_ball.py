"""
File: bouncing_ball.py
Name: Hank周柏翰
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball')
ball = GOval(SIZE, SIZE)
ball.filled = True
t = 0  # The on/off button, when t == 0: on, when t == 1: off
count = 0  # count controls the times that the ball bounces


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)


def bouncing(m):
    global t
    global count
    v_y = 0  # The initial velocity of y direction
    if t == 0 and count < 3:  # when count equals to 3, we will not run the program anymore.
        t = t+1  # t==1 to ensure that mouseclick will not interrupt the procedure.
        window.add(ball, START_X, START_Y)
        while (ball.x+ball.width) < 800:
            ball.move(VX, v_y)
            pause(DELAY)
            v_y = v_y + GRAVITY
            if (ball.y+ball.height) >= 500:
                v_y = v_y * REDUCE  # 反彈瞬間
                while v_y > 0:
                    ball.move(VX, -v_y)
                    v_y = v_y - GRAVITY
                    pause(DELAY)
        count = count+1  # 'count' controls the times that the ball bounces.
        window.add(ball, START_X, START_Y)
        t = t-1  # t goes back to 0










if __name__ == "__main__":
    main()
