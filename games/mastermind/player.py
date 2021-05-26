import random 

pegs = ['blue', 'yellow', 'green', 'red']

class Player():
	def create_guess_code(self, pegs):
		"""
		Creates a randomized new code

		Args:
			pegs (list): The colored pegs list

		Returns:
			pegs (list): The randomized colored pegs list
		"""
		random.shuffle(pegs)
		
		return pegs

# Se debería de poder elegir si es pc-pc, pc-jugador, jugador-pc, jugador-jugador
# player (clase mama) --> person (clase hija)
# player (clase mama)  --> pc (clase hija)
# elegir pegs para adivinar
# decidir si los pegs son correctos

guess_code = player().create_guess_code(pegs)
print(guess_code)
