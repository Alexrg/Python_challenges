"""
Write a Python function name_lookup that takes a string first_name that
corresponds to one of "Joe", "Scott", "John" or "Stephen") and then returns
their corresponding last name "Warren", "Rixner", "Greiner" or "Wong"). If
first_name doesn't match any of those strings, return the
string "Error : Not an instructor".
"""
def name_lookup(first_name):
	instructors  = {
		'Joe': 'Warren',
		'Scott': 'Rixner',
		'John': 'Greiner',
		'Stephen': 'Wong'
	}

	instructor = instructors.get(first_name)
	
	if instructor == None :
		instructor = "Error: The name entered does not belong to an instructor"
	
	return instructor

first_name = 'Carmen'

print(name_lookup(first_name))