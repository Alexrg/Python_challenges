import random


class Quicksort():
	"""
	QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and
	partitions the given array around the picked pivot.
	"""
	def __init__(self):
		self.integer_list = self.create_list()

	def create_list(self):
		"""
		Creates a 10 element list, with random numbers from 0 to 500.

		Returns:
			random_list (array): A list containing random numbers from 0 to 500.
		"""

		random_list = random.sample(range(0, 500), 10)

		return random_list

number_list = Quicksort().integer_list
print(number_list)