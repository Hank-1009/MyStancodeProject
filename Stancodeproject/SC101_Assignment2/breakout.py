"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts
# global variable
start = False  # 滑鼠點擊才開始的開關
start_1 = False  # 避免球在板子震盪的一個開關
life = NUM_LIVES
score = 0


def main():
    global start
    global life
    global score
    global start_1
    graphics = BreakoutGraphics()
    score = graphics.r * graphics.c
    ball = graphics.ball  # To simplify the coding
    paddle = graphics.paddle
    window = graphics.window  # To simplify the coding
    dx = graphics.speed_x
    dy = graphics.speed_y
    onmouseclicked(go)
    # Add animation loop here!
    while True:
        if start:  # We start the while loop when start == True
            #  基本的反彈條件
            ball.move(dx, dy)
            if (ball.x + ball.width) > window.width or ball.x < 0:
                dx = -dx
                start_1 = False
            if ball.y < 0:  # y方向只有上層才須反彈
                dy = -dy
                start_1 = False
            if ball.y > window.height:
                life -= 1
                start_1 = False
                if life == 0:
                    break
                start = False
                window.add(ball, x=(window.width - ball.width) / 2, y=(window.height - ball.width) / 2)
            """
            #遇到磚塊或板子的反彈
            1. First, we check the 4 points of our ball with obj1,2,3,4 
            """
            obj1 = window.get_object_at(ball.x, ball.y)
            obj2 = window.get_object_at(ball.x + ball.width, ball.y)
            obj3 = window.get_object_at(ball.x, ball.y + ball.width)
            obj4 = window.get_object_at(ball.x + ball.width, ball.y + ball.width)
            """
            2. Second, make sure that each point will not repeat getting the same object and paddle.
            3. start_1 ensure us not to let the ball stick on the paddle.
            4. score tells us when to break the game.(score=0, it ends)
            """
            if obj1 is not None:
                if obj1 is not paddle:
                    window.remove(obj1)
                    start_1 = False
                    score -= 1
                    dy = -dy
            if obj2 is not None:
                if obj2 is not paddle and obj2 is not obj1:
                    window.remove(obj2)
                    start_1 = False
                    score -= 1
                    dy = -dy
            if obj3 is not None:
                if obj3 is not paddle and obj3 is not obj2 and obj3 is not obj1:
                    window.remove(obj3)
                    start_1 = False
                    score -= 1
                    dy = -dy
            if obj4 is not None:
                if obj4 is not paddle and obj4 is not obj3 and obj4 is not obj2 and obj4 is not obj1:
                    window.remove(obj4)
                    start_1 = False
                    score -= 1
                    dy = -dy
            # Now, we define another condition for getting paddle
            if obj1 is paddle or obj2 is paddle or obj3 is paddle or obj4 is paddle:
                if (ball.y+ball.width-10) and not start_1:  # 這裡-2.8是因為ball.y在碰到paddle時實際上y座標會超出約2.5
                    print(ball.y + ball.height - paddle.y)
                    dy = -dy
                    start_1 = True
            if score == 0:
                break
        pause(FRAME_RATE)


def go(m):
    global start
    start = True


if __name__ == '__main__':
    main()
