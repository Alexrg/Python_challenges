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

	def full_name(self):
		"""
		Returns the full name for a person as a string, which is the first name
		followed by a space, followed by the last name

		Returtns:
			full_name (string): Full name of the person
		"""
		
		full_name = "{} {}".format(self.first_name, self.last_name)
		return full_name

alejandra = Person("Alejandra", "Rodríguez",1992)
print(alejandra.full_name())