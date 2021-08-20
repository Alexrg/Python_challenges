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

print(divisors(34))