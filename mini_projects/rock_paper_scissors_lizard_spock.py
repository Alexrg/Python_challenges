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

number_choice = name_to_number('lizard')
print(number_choice)

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

name_choice = number_to_name(3)
print(name_choice)