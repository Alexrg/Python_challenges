"""
Create a function that opens the flowers.txt, reads every line in it, and saves
it as a dictionary. The main (separate) function should take user input (user's
first name and last name) and parse the user input to identify the first letter
of the first name. It should then use it to print the flower name with the same
first letter (from dictionary created in the first function).
"""

def read_file(file):
	"""
	From the receibed text file, extract each text line into an array.

	Args:
		file (string): The filename.

	Returns:
		lines (list): The list containing the text lines.
	"""
	lines = []
	
	with open("flowers.txt") as flowers_file:
	    lines = flowers_file.readlines()
	
	return lines

def create_dictionary(flower_list):
	"""
	From the receibed list, create a dictionary with the flower_list.

	Args:
		flower_list (list): A list with the flowers and first letter.

	Returns:
		flower_dictionary (dictionary): A dictionary that pairs the flower with it's
										inital letter.
	"""
	flower_dictionary = {}

	for flower in flower_list:
		flower_dictionary[flower.split(":")[0]] = flower.split(":")[1]

	return flower_dictionary


lines = read_file("flowers.txt")
flower_dictionary = create_dictionary(lines)
user_name = input('Enter your name: ').capitalize()
unique_flower = flower_dictionary[user_name[0]]

print("Unique flower name with the first letter: {}".format(unique_flower))

