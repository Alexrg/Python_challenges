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

first_name = 'Joe'
name_lookup(first_name)

def day_lookup(weekday):
	"""
	Given a day of the week, returns a number that represents it. If the given text
	is not a weekday, it returns an error.

	Args:
		weekday (string): The day of the week.

	Returns:
		weekday_number (number or string): Returns a text with an error it the received
										   string is not a weekday or if it is a correct
										   weekday, it returns the asigned number.
	"""
	weekday_dictionary = {
		'Sunday':0,
		'Monday':1,
		'Tuesday':2,
		'Wednesday':3,
		'Thursday':4,
		'Friday':5,
		'Saturday':6,
	}

	weekday_number = weekday_dictionary.get(weekday.capitalize())
	
	if weekday_number == None :
		weekday_number = "Error: The text entered ({}) does not belong to any weekday, check your spelling.".format(weekday)

	return weekday_number

weekday = 'thuesdayr'
day_lookup(weekday)