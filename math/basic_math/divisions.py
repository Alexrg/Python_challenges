"""
Write a function that takes two integers (x and y) and returns a list of numbers
between x and y that are divisible by 5 but not by 7.
"""

def divisibility(x,y):
	"""
	Take two integers (x and y) and returns a list of numbers between x and y that
	are divisible by 5 but not by 7.

	Args:
		x (int): The lower number range entered by the user
		y (int): The upper number range entered by the user

	Returns:
		divisibility_list (list): A list with the numbers in range between x and that
								  are divisible by 5 but not by 7.
	"""
	divisibility_list = []
	for number in range(x+1,y):
		if number % 5 == 0:
			if number % 7 == 0:
				continue
			divisibility_list.append(number)

	return divisibility_list

print('You will enter two numbers')

x = int(input('Enter the lower range number : '))
y = int(input('Enter the upper range number : '))

number_list = divisibility(x,y)

print(number_list)