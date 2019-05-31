"""
The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its
sides. Write a Python statement that calculates and prints the length in
inches of the perimeter of a rectangle with sides of length 4 and 7 inches.
"""
def rectangle(width, heigth):
	"""
	Convert distance units from miles to feet
	Args:
		width (number): Width of the rectangle
		heigth (number): Heigth of the rectangle

	Returns:
		perimeter (number): The calculated perimeter of the rectangle
	"""
	perimeter = 2 * width + 2 * heigth
	return perimeter

perimeter = rectangle(4,7)