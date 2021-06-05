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

	def choose_pivot(self,number_list):
		"""
		To choose the pivot number, divide the list in half so the middle number
		is the pivot.

		Returns:
			pivot_number (integer): The pivot number of the list
		"""
		pivot_index = int(len(number_list)/2)
		pivot_number = number_list[pivot_index]

		return pivot_number

	def order_list(self):
		"""
		"""
		pivot_number = self.choose_pivot(self.integer_list)
		ordered_list = [pivot_number]

		for number in self.integer_list:
			if number > pivot_number:
				ordered_list.append(number)
			elif number < pivot_number:
				ordered_list.insert(0,number)

		return ordered_list


quicksort_method = Quicksort()
number_list = quicksort_method.integer_list
print(number_list)
print(quicksort_method.order_list())