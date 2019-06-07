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

"""
There are several ways to calculate the area of a regular polygon. Given the
number of sides, nn, and the length of each side, s, the polygon's area is: 
ns^2 / 4tan(n / π)
​For example, a regular polygon with 5 sides, each of length 7 inches, has an
area of 84.3033926289 square inches. Write a function that calculates the area
of a regular polygon, given the number of sides and length of each side. Submit
the area of a regular polygon with 7 sides each of length 3 inches. Enter a
number (and not the units) with at least four digits of precision after the
decimal point. Note that the use of inches as the unit of measurement in these
examples is arbitrary. Python only keeps track of the numerical values, not
the units.
"""
def polygon_area(number_of_sides, side_length):
	"""
	Calculate the area of a polygon given the number of sides and their length
	Args:
		number_of_sides (number): Number of sides of the polygon
		side_length (number): Size of the polygon sides

	Returns:
		area (number): The calculated area of the polygon
	"""
	area = (number_of_sides * math.pow(side_length,2)) / (4 * math.tan(math.pi/number_of_sides))
	return area

polygon = polygon_area(7, 3)
print("The area of a 7 sides polygon is {}".format(polygon))
