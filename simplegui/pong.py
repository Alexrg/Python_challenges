import simplegui
import random

"""
Challenge: Implementation of classic arcade game Pong

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive Pong game.
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

def new_game():
    """
    Initiate a new Pong game spawning the ball in a random direction

    Global:
        paddle1_pos (Number): The position of the paddle in the left
        paddle2_pos (Number): The position of the paddle in the right
        paddle1_vel (Number): The velocity of the paddle in the left
        paddle2_vel (Number): The velocity of the paddle in the right
        score1 (Number): The score of the player in the left
        score2 (Number): The score of the player in the right

    """
    global paddle1_pos
    global paddle2_pos
    global paddle1_vel
    global paddle2_vel 
    global score1
    global score2  
    
    score1 = 0
    score2 = 0

    direction = [LEFT, RIGHT]

    spawn_ball(direction[random.randint(0,1)])

def draw(canvas):
    """
    Draw the elements of the pong game

    Global:
        paddle1_pos (Number): The position of the paddle in the left
        paddle2_pos (Number): The position of the paddle in the right
        paddle1_vel (Number): The velocity of the paddle in the left
        paddle2_vel (Number): The velocity of the paddle in the right
        ball_pos (List): The position of the ball in x and y coordinates
        ball_vel (List): The velocity of the ball in x and y coordinates
        score1 (Number): The score of the player in the left
        score2 (Number): The score of the player in the right
    """
    
    global paddle1_pos
    global paddle2_pos
    global paddle1_vel
    global paddle2_vel
    global ball_pos
    global ball_vel
    global score1
    global score2  

    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    if paddle1_pos > 300 or paddle1_pos < 0:
        paddle1_vel = 0
    if paddle2_pos > 300 or paddle2_pos < 0:
        paddle2_vel = 0 
    
    # draw paddles
    canvas.draw_line([0, paddle1_pos], [0, paddle1_pos+100], 15, 'Green')
    canvas.draw_line([600, paddle2_pos], [600, paddle2_pos+100], 15, 'Red')
    
    # determine whether paddle and ball collide 
    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH:
        if paddle1_pos < ball_pos[1] and paddle1_pos + 100 > ball_pos[1]:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(LEFT)
            score2 += 1
    elif ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH:
        if paddle2_pos < ball_pos[1] and paddle2_pos + 100 > ball_pos[1]:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(RIGHT)
            score1 += 1       
    elif ball_pos[1]-BALL_RADIUS <= 0 or ball_pos[1]+BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    
    # draw scores
    canvas.draw_text("You: {}".format(score1), [20,10], 15, "Green")
    canvas.draw_text("CPU: {}".format(score2), [530,10], 15, "Red")

def keydown(key):
    """
    Change the velocity of the paddle every time any of the player enters a key

    Global:
        paddle1_vel (Number): The velocity of the paddle in the left
        paddle2_vel (Number): The velocity of the paddle in the right
    """
    global paddle1_vel
    global paddle2_vel

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 2
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 2
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -2