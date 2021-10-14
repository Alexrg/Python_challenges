"""
Write a generator that takes a number N and returns all perfect squares less
than N. Hint: use yield.
- Example 1: N=30 then the generator will give 1,4,9,16,25
"""
from math import sqrt

def perfect_square_generator(range_limit):
	"""
	Takes a number N and returns all perfect squares less than N.

	Args:
		range_limit (number): The user inputs a limit upper rage to evaluate.

	Yields:
		number (number): Yields a number if its a perfect square.
	"""
	for number in range(1,range_limit+1):
		if sqrt(number).is_integer():
			yield number

range_limit = int(input('Enter the upper range number : '))

for square_number in perfect_square_generator(range_limit):
	print(square_number)