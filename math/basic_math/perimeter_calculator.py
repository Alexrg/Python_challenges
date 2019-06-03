import math

"""
The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its
sides. Write a Python statement that calculates and prints the length in
inches of the perimeter of a rectangle with sides of length 4 and 7 inches.
"""
def rectangle_perimeter(width, heigth):
	"""
	Calculate the perimeter of a rectangle
	Args:
		width (number): Width of the rectangle
		heigth (number): Heigth of the rectangle

	Returns:
		perimeter (number): The calculated perimeter of the rectangle
	"""
	perimeter = 2 * width + 2 * heigth
	return perimeter

rectangle = rectangle_perimeter(4,7)

"""
Write a Python function circle_circumference that takes a single parameter
radius corresponding to the radius of a circle in inches and returns the the
circumference of a circle with radius radius in inches. Do not use π = 3.14,
instead use the math module to supply a higher-precision approximation to π.
"""
def circle_circunference(diameter):
	"""
	Calculate the circunference of a circle
	Args:
		diameter (number): The area of the cirle will be calculated using the diameter

	Returns:
		circunference (number): The calculated circunference of the circle
	"""
	circunference = math.pi * diameter
	return circunference

circle = circle_circunference(35.5)
print(circle)