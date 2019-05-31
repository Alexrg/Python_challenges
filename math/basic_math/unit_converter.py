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


"""
Write a Python statement that calculates and prints the number of
seconds in 7 hours, 21 minutes and 37 seconds.
"""
def time_to_seconds(hours, minutes, seconds):
	hours_to_seconds = 60 * 60 * hours
	minutes_to_seconds = 60 * minutes

	total_seconds = hours_to_seconds + minutes_to_seconds + seconds

	return total_seconds

hours = 7
minutes = 21
seconds = 37
print(time_to_seconds(hours, minutes, seconds))