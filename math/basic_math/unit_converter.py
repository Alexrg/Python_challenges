"""
There are 5280 feet in a mile. Write a Python statement
that calculates and prints the number of feet in 13 miles
"""
def miles_to_feet(miles):
	"""
	Convert distance units from miles to feet
	Args:
		miles (number): Miles that will be converted into feet

	Returns:
		sum_digits (number): Miles converted into feet units
	"""
	feet = 5280 * miles
	return feet

miles = 13
feet = miles_to_feet(miles)