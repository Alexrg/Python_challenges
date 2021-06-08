import random 

pegs = ['blue', 'yellow', 'green', 'red', 'white', 'pink']

class Player():
	def create_guess_code(self, pegs):
		"""
		Creates a randomized new peg code of four colors.

		Args:
			pegs (list): The colored pegs list

		Returns:
			selected_pegs (list): The randomized four elements of colored pegs list.
		"""
		selected_pegs = random.sample(pegs, 4)
		
		return selected_pegs

guess_code = Player().create_guess_code(pegs)
print(guess_code)