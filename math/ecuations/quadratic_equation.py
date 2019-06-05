import math
"""
Given numbers a, b, and c, the quadratic equation a x^2 + b x + c = 0 can have
zero, one or two real solutions (i.e; values for x that satisfy the equation).
The quadratic formula x = − b ± (b^2 − 4ac)^1/2 / 2a can be used to compute
these solutions. The expression b^2 - 4ac is the discriminant associated with
the equation. If the discriminant is positive, the equation has two solutions.
If the discriminant is zero, the equation has one solution. Finally, if the
discriminant is negative, the equation has no solutions. Write a Python function
smaller_root that takes an input the numbers a, b and c and returns the smaller
solution to this equation if one exists. If the equation has no real solution,
print the message "Error: No real solutions" and simply return. Note that, in
this case, the function will actually return the special Python value None.
"""
def smaller_root(value_a, value_b, value_c):
	"""
	Find the number of solutions the quadratic function would have according
	to the discriminant
	
	Args:
		value_a (number): The value of the variable a
		value_b (number): The value of the variable b
		value_c (number): The value of the variable c

	Returns:
		solutions (number): Number of solutions
	"""
	
	# The disctiminant formula to evaluate the number of solutions
	discriminant_expression = math.pow(value_b, 2) - (4 * value_a * value_c)
	
	solutions = 1

	if discriminant_expression > 0 :
		solutions = 2
	elif discriminant_expression < 0 :
		solutions = "No real solutions"

	return solutions

value_a = 20
value_b = 10
value_c = 30

number_of_solutions = smaller_root(value_a, value_b, value_c)
print("There are {} solutions".format(number_of_solutions))