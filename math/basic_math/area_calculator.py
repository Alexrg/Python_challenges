"""
Write a Python function rectangle_area that takes two parameters width and
height corresponding to the lengths of the sides of a rectangle and returns
the area of the rectangle in square inches
"""
def rectangle_area(width, height):
	"""
	Calculate the area of a rectangle
	Args:
		width (number): Width of the rectangle
		heigth (number): Heigth of the rectangle

	Returns:
		area (number): The calculated area of the rectangle
	"""
	area = width * height
	return area

rectangle = rectangle_area(4,5)