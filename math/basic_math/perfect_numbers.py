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
	"""
	total_sum = 0

	for number in divisors_list:
		total_sum += number

	return total_sum

get_divisors = divisors(6)
print(get_divisors)
print(sum_numbers(get_divisors))