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

deck_one = list(range(0, 8))
deck_two = list(range(0, 8))
decks = deck_one + deck_two
exposed = [True,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False]
card_pos = []
game_status = 0
exposed_card = []
exposed_card_index = []
turns = 0

# helper function to initialize globals
def new_game():
    """
    Shuffles randomly the cards deck every new game
    """
    global decks
    global exposed
    global game_status
    global turns
    
    exposed = [False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False]
    random.shuffle(decks)
    game_status = 0
    turns = 0
    turns_label.set_text('Turns: {}'.format(turns))

     
# define event handlers
def mouseclick(pos): 
    """
    Logic of the game. State 0 corresponds to the start of the game. In state 0, if
    you click on a card, that card is exposed, and you switch to state 1. State 1
    corresponds to a single exposed unpaired card. In state 1, if you click on an
    unexposed card, that card is exposed and you switch to state 2. State 2
    corresponds to the end of a turn. In state 2, if you click on an unexposed card,
    that card is exposed and you switch to state 1.
    
    globals:
        exposed (array): An array that contains a truth value of exposure for every card
                         in the deck, true for exposed and false for face down.
        game_status (number): The status of the current game.
        exposed_card (array): The exposed cards in order in which they were exposed
        exposed_card_index (array): The deck index of the exposed cards in order in
                                    which they were exposed.
    """
    global exposed
    global game_status
    global exposed_card
    global exposed_card_index
    global turns
    
    for card in range(0,len(exposed)):
        if pos[0] >= card_pos[card] and pos[0] <= card_pos[card]+40:
            
            if exposed[card] == False: 
                exposed[card] = True 
                exposed_card.append(decks[card])
                exposed_card_index.append(card)
                if game_status == 2:
                    if exposed_card[0] == exposed_card[1]:
                        del exposed_card[0:2]
                        del exposed_card_index[0:2]
                        game_status = 0
                    else:
                        exposed[exposed_card_index[0]] = False
                        exposed[exposed_card_index[1]] = False
                        del exposed_card[0:2]
                        del exposed_card_index[0:2]
                        game_status = 0
                game_status += 1
                turns += 1
                turns_label.set_text('Turns: {}'.format(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    """
    Draws the deck in the frame
    """
    global card_pos
    
    card_pos = []
    
    for card_index, card in enumerate(decks):
        card_pos.append((50 * card_index)+10)
        if exposed[card_index] == False:
            canvas.draw_polygon([(card_pos[card_index],10), (card_pos[card_index]+40,10), (card_pos[card_index]+40,90),(card_pos[card_index],90),(card_pos[card_index],10)], 2, 'Red')
        else:
            canvas.draw_text(str(card), (card_pos[card_index]+10,60), 40, 'Red')
            canvas.draw_polygon([(card_pos[card_index],10), (card_pos[card_index]+40,10), (card_pos[card_index]+40,90),(card_pos[card_index],90),(card_pos[card_index],10)], 2, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 810, 100)
frame.add_button("Reset", new_game)
turns_label = frame.add_label('Turns:')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric