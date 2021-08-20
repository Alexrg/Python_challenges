"""
Create a program that will find if a number and properly classify
it as a perfect number.
"""

def divisors(integer):
    """
    Find all the divisors of the given number.

    Args:
    	integer (int): A given number.

    Returns:
    	divisors (list): The divisors of the given number in a list format.
    """
    divisors = []
    
    for number in range(1,integer):
        if integer != number:
            if integer % number== 0:
                divisors.append(number)
        else:
            pass
    
    return divisors

def sum_numbers(divisors_list):
	"""
	Sum the numbers of the given list.
    
    Args:
    	divisors_list (list): The list of the divisors of a number.

    Returns:
    	total_sum (number): Sum the numbers of the given list.	
	"""
	total_sum = 0

	for number in divisors_list:
		total_sum += number

	return total_sum

def classify_number(number):
	"""
	Classifies the given number. If the sum of the divisors is larger than the
	number, it's an abundant number, if the sum is smaller, it's called an
	deficient number, but if the sum is equal to the number, then it's a
	perfect number.
    
    Args:
    	number (int): A given number.

    Returns:
    	(string): Prompts the clasification of the number.
	"""
	get_divisors = divisors(number)
	sum_divisors = sum_numbers(get_divisors)
	
	if sum_divisors > number:
		return "%d is an abundant number" % number
	elif sum_divisors == number:
		return "%d is a perfect number" % number
	elif sum_divisors < number:
		return "%d is a deficient number" % number

print(classify_number(8128))