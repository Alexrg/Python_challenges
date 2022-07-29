#Write a function called count_capital_consonants. This
#function should take as input a string, and return as output
#a single integer. The number the function returns should be
#the count of characters from the string that were capital
#consonants. For this problem, consider Y a consonant.
#
#For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0

#Write your function here!
def count_capital_consonants(given_string):
    """
    Takes as input a string, and return as output 
    a single integer. The number the function returns
    should be the count of characters from the string
    that were capital consonants. For this problem,
    consider Y a consonant.
    
    Args:
        given_string (string): An input string.
        
    Returns:
        capital_consonant_count (int): the count of
        characters from the string that were capital
        consonants
    """
    capital_consonant_count = 0
    vowels = ["A","E","I","O","U"]
    
    for letter in given_string:
        if letter.isupper() and letter not in vowels:
            capital_consonant_count += 1
    
    return capital_consonant_count
