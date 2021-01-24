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

lines = read_file("flowers.txt")
print(lines)