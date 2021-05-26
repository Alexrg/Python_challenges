import random

def create_list():
	"""
	Creates a 10 element list, with random numbers from 0 to 500.

	Returns:
		random_list (array): A list containing random numbers from 0 to 500.
	"""

	random_list = random.sample(range(0, 500), 10)

	return random_list