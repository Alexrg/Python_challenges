"""
Kristen loves playing with and comparing numbers. She thinks that if she takes
two different positive numbers, the one whose digits sum to a larger number
is better than the other. If the sum of digits is equal for both numbers,
then she thinks the smaller number is better. For example, Kristen thinks that
13 is better than 31 and that 12 is better than 11 Given an integer, n, can
you find the divisor n of that Kristin will consider to be the best?

Input formtat
A single integer denoting n

Constraints
0 < n < 10^5

Output format
Print an integer denoting the best divisor of n
"""

# Read the input numbers
print("Enter the first number: ")
first_number = input()
print("Enter the second number: ")
second_number = input()

"""
1. Convert the number to string
2. Separate the elements on the array
3. Convert the elements to integer to sum them
"""
def sum_digits(number):
	"""
	Convert the number to a string, then sums the digits of that array by
	converting each separate element of the array to integer and adding it
	in a different variable

	Args:
		number: The number entered by the user

	Returns:
		sum_digits: Sums all the digits of the number in the argument
	"""
	number_in_string = str(number)
	sum_digits = 0
	
	for digit in number_in_string:
		sum_digits += int(digit)

	return sum_digits

def get_smaller_number(first_number,second_number):
	"""
	Get the smaller number from both of the numbers entered by the user

	Args:
		first_number: The first number entered by the user
		second_number: The second number entered by the user

	Returns:
		smaller_number: The smaller number between both numbers
	"""
	smaller_number = 0

	if (first_number > second_number):
		smaller_number = second_number
	elif (first_number < second_number):
		smaller_number = first_number

	return smaller_number

# 4. Compare
def compare_numbers_digits(first_number,second_number):
	"""
	Sum the digits of two different numbers, the one whose digits sum to a
	larger number is better than the other. If the sum of digits is
	equal for both numbers, then the smaller number is better.

	Args:
		first_number: The first number entered by the user
		second_number: The second number entered by the user

	Returns:
		best_number: The best number according to the comparision
	"""
	first_number_digits = sum_digits(first_number)
	second_number_digits = sum_digits(second_number)

	best_number = 0

	if(first_number_digits == second_number_digits):
		best_number = get_smaller_number(first_number,second_number)
	elif(first_number_digits > second_number_digits):
		best_number = first_number
	elif(first_number_digits < second_number_digits):
		best_number = second_number

	return best_number

def compare_numbers(first_number,second_number):
	"""
	Compare if if numbers are equal or different. If numbers are equal, then
	none of them is better than the other, if they are different get the
	best number.

	Args:
		first_number: The first number entered by the user
		second_number: The second number entered by the user

	Returns:
		message: The message with the best number if any
	"""
	mesage = ""
	
	if(first_number == second_number):
		message = "There is no best number"
	else:
		best_number = compare_numbers_digits(first_number,second_number)
		message = "The best number is: {}".format(best_number)

	return message

best_number = compare_numbers(first_number,second_number)
print(best_number)







