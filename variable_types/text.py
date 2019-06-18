"""
Write a Python function name_tag that takes as input the parameters first_name
and last_name (strings) and returns a string of the form "My name is % %."
where the percents are the strings first_name and last_name. Reference the test
cases in the provided template for an exact description of the format of the
returned string.
"""
def name_tag(first_name, last_name):
	"""
	Get a text with the full name of a person
	
	Args:
		first name (string): First name of a person
		last name (string): Last name of a person

	Returns:
		full_name (string): Text with the full name of a person
	"""
	full_name = "My name is {} {}".format(first_name, last_name)
	return full_name

full_name = name_tag('Alejandra', 'Rodriguez')
print(full_name)


"""
Given the program template below, write a Python function print_goodbye() that
defines a local variable message whose value is "Goodbye" and prints the value
of this local variable to the console. Note that the existing global variable
message retains its original value "Hello" after the call to print_goodbye() 
"""
def print_goodbye():
	"""
	Returns a "Goodbye" message to the user

	Returns:
		messafe (string): A "Goodbye" message to the user
	"""
	message = "Goodbye"
	return message


def print_hello():
	"""
	Returns a "Goodbye" message to the user

	Returns:
		messafe (string): A "Goodbye" message to the user
	"""
	message = "Hello"
	return message