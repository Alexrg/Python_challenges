import simplegui
import random

"""
Challenge: Implementation of classic arcade game Pong

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False

paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = 0
paddle2_pos = 0
score1 = 0
score2 = 0
ball_pos = [0,0]
ball_vel = [0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    """
    Initiate the ball in the middle of the table in direction to the last
    player who won

    Args:
        direction (Boolean): If the direction is Left, boolean is True and if
                             it's Rigth it will be False

    Global:
        ball_pos (List): The position of tha ball
        ball_vell (List): The velocity of tha ball
    """

    global ball_pos
    global ball_vel 
    
    ball_pos = [300, 200]
    if direction == True:
        ball_vel = [.9,  -0.7]
    elif direction == False:
        ball_vel = [-.9,  0.7]