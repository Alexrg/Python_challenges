import random
"""
Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors
that allows five choices. Each choice wins against two other choices, loses
against two other choices and ties against itself. Much of RPSLS's popularity
is that it has been featured in 3 episodes of the TV series
"The Big Bang Theory"
"""

def name_to_number(name):
	"""
	Given the name of the game choices, returns the number it represents in the game
	
	Args:
		name (string): The name of the choice given by the player

	Returns:
		number_choice (number): The number that represents the given choice
	"""
	game_choices = {
		'rock':0,
		'paper':1,
		'scissors':2,
		'lizard':3,
		'spock':4
	}

	# Get the number from the dictionary
	number_choice = game_choices.get(name)

	# If the given choice is not a vaild one
	if number_choice == None:
		number_choice = 'The given name is not a valid game choice'

	return number_choice

def number_to_name(number):
	"""
	Given the number of the game choices, returns the name it represents in the game
	
	Args:
		number_choice (number): The number given by the player that represents
								the given choice

	Returns:
		name (string): The name of the game choice
	"""
	game_choices = {
		0 : 'rock',
		1 : 'paper',
		2 : 'scissors',
		3 : 'lizard',
		4 : 'spock'
	}

	# Get the name from the dictionary
	name_choice = game_choices.get(number)

	# If the given choice is not a vaild one
	if name_choice == None:
		name_choice = 'The given number is not a valid game choice'

	return name_choice

def rpsls(player_choice):
    """
	Get the player's choice and calculate the computer's to then calculate
	who is the winner.
	
	Args:
		player_choice (number): The player enters a choice choice
	
	Returns:
		winner (string): A string prompting wether the computer or the player won
	"""
	# Print the available options in the game
    print("""
    Choose from the following options:
    0 : ‘rock’
    1 : ‘paper’
    2 : ‘scissors’
    3 : ‘lizard’
    4 : ‘spock’
    """)
    
    # Prompt the player and computer choices
    player_number = name_to_number(player_choice)
    player_choice_string = "Player chooses {}".format(player_choice)
    print(player_choice_string)
    comp_number = random.randint(0,4)
    comp_choice = "Computer chooses {}".format(number_to_name(comp_number))
    print(comp_choice)

    # Get the difference of the points between both player options
    diference_points = player_number - comp_number

    # Calculate the winner 
    winner = "It's a tie!"

    if diference_points > 0 :
    	winner = "Player wins!"
    elif diference_points < 0 :
    	winner = "Computer wins!"

    print(winner)
    
    return winner

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
