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

	def choose_pivot(self):
		"""
		To choose the pivot number, divide the list in half so the middle number
		is the pivot.

		Returns:
			pivot_number (integer): The pivot number of the list
		"""
		pivot_index = int(len(self.integer_list)/2)
		pivot_number = self.integer_list[pivot_index]

		return pivot_number

quicksort_method = Quicksort()
number_list = quicksort_method.integer_list
pivot_number = quicksort_method.choose_pivot()
print(number_list)
print(pivot_number)