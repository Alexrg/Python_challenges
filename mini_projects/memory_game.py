import simplegui
import random

"""
Memory is a card game in which the player deals out a set of cards face down. In
Memory, a turn (or a move) consists of the player flipping over two cards. If
they match, the player leaves them face up. If they don't match, the player
flips the cards back face down. The goal of Memory is to end up with all of the
cards flipped face up in the minimum number of turns. For this project, we will
keep our model for Memory fairly simple. A Memory deck consists of eight pairs
of matching cards.

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""

deck_one = list(range(0, 9))
deck_two = list(range(0, 9))
decks = deck_one + deck_two

# helper function to initialize globals
def new_game():
    """
    Shuffles randomly the cards deck every new game
    """
    pass

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    """
    Draws the deck in the frame
    """
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric