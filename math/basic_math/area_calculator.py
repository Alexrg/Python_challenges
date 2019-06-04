import math
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

"""
Write a Python function circle_area that takes a single parameter radius
corresponding to the radius of a circle in inches and returns the the area of a
circle with radius radius in square inches. Do not use π = 3.14, instead use the
math module to supply a higher-precision approximation to π.
"""
def circle_area(radius):
	"""
	Calculate the area of a circle given the radius
	Args:
		radius (number): The radius of a circle

	Returns:
		area (number): The calculated area of the circle
	"""
	area = math.pi * math.pow(radius, 2)
	return area

circle = circle_area(35)