"""
Write a Python function name_lookup that takes a string first_name that
corresponds to one of "Joe", "Scott", "John" or "Stephen") and then returns
their corresponding last name "Warren", "Rixner", "Greiner" or "Wong"). If
first_name doesn't match any of those strings, return the
string "Error : Not an instructor".
"""
def name_lookup(first_name):
	"""
	Given the first name of the instructor, returns the last name gotten
	from the dictionary
	
	Args:
		first_name (string): First name of the instructor

	Returns:
		last_name (string): Last name of the instructor
	"""
	# Dictionary with all the instructors' names
	instructors  = {
		'Joe': 'Warren',
		'Scott': 'Rixner',
		'John': 'Greiner',
		'Stephen': 'Wong'
	}

	last_name = instructors.get(first_name)
	
	if last_name == None :
		last_name = "Error: The name entered does not belong to an instructor"
	
	return last_name

first_name = 'Carmen'
name_lookup(first_name)