"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # cols and rows
        self.c = brick_cols
        self.r = brick_rows
        self.p_offset = paddle_offset
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - self.paddle.width) / 2,
                        y=(window_height - paddle_offset - self.paddle.
                           height))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius*2) / 2, y=(window_height - ball_radius*2) / 2)
        # Default initial velocity for the ball
        self._dy = INITIAL_Y_SPEED
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        # Initialize our mouse listeners
        onmousemoved(self.reset_position)
        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                brick.filled = True
                if j < BRICK_ROWS / 5:  # I divide the bricks into 5 groups by rows, and assign different color.
                    brick.fill_color = 'red'
                elif j < BRICK_ROWS / 5 * 2:
                    brick.fill_color = 'orange'
                elif j < BRICK_ROWS / 5 * 3:
                    brick.fill_color = 'yellow'
                elif j < BRICK_ROWS / 5 * 4:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick, x=i * (BRICK_SPACING + BRICK_WIDTH),
                                y=j * (BRICK_SPACING + BRICK_HEIGHT) + BRICK_OFFSET)
                # put the bricks on window respectively.

    def reset_position(self, mouse):
        if (self.paddle.width / 2) <= mouse.x <= (self.window.width - self.paddle.width / 2):
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x < self.paddle.width / 2:
            self.paddle.x = 0






    # Two getters to get velocity
    @property
    def speed_x(self):
        return self._dx

    @property
    def speed_y(self):
        return self._dy
