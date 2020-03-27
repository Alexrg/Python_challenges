"""
As your first task, implement a Person class which has the fields first_name, last_name and birth_year.
This class should include the methods: __init__ which takes strings for the two name fields and an
integer for the year of birth, full_name returns the full name for a person as a string, which is
the first name followed by a space, followed by the last name, age which takes the current year as
input and returns the age in years of the person (Don't worry about days and months here, just return
the difference of the two years.), and __str__ returns a string that includes the first name and last
name of the person as well as their year of birth. Definition of Person class template
"""
class Person():
	def __init__(self, first_name, last_name, birth_year):
		"""
		Creates an object person that receives it's first name, last name and
		birth year.

		Args:
			firts_name (string): The person's first name
			last_name (string): The person's last name
			birth_year (int): The person's birth year
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.birth_year = birth_year

alejandra = Person("Alejandra", "Rodríguez",1992)
print(alejandra.birth_year)