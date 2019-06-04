"""
Write a Python function is_even that takes as input the parameter number (an
integer) and returns True if number is even and False if number is odd. Hint:
Apply the remainder operator to n (i.e., number % 2) and compare to zero.
"""
def is_even(number):
	"""
	Evaluate if the given number is either Even (True) or Odd (False)
	Args:
		number (number): The number that will be evaluated

	Returns:
		evaluate_number (boolean): True if the number is Even or False if its Odd
	"""
	even_evaluation = False
	if number % 2 == 0 :
		even_evaluation = True

	return even_evaluation

evaluate_number = is_even(44)