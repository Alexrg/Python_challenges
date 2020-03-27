class Person():
	def __init__(self, first_name, last_name, birth_year):
		"""
		Creates an object person that receives it's first name, last name and
		birth year.

		Args:
			firts_name (string): The person's first name
			last_name (string): The person's last name
			birth_year (number): The person's birth year
		"""
		
		self.first_name = first_name
		self.last_name = last_name
		self.birth_year = birth_year

	def __str__(self):
		"""
		Returns all the information of the person in form of a string

		Returns:
			personal_information (string): The information of the person
		"""
		
		personal_information = "The person's name is {}, their birth year is {}".format(self.full_name(), self.birth_year)
		return personal_information

	def full_name(self):
		"""
		Returns the full name for a person as a string, which is the first name
		followed by a space, followed by the last name

		Returtns:
			full_name (string): Full name of the person
		"""
		
		full_name = "{} {}".format(self.first_name, self.last_name)
		return full_name

	def age(self, current_year):
		"""
		Retrurns the age of the person by substracting it's birth year from the
		current year
		
		Args:
			current_year (number): The current year

		Returtns:
			age (number): The age of the person
		"""

		age = current_year - self.birth_year
		return age

def average_age(persons_list, current_year):
	"""
	Retrurns the age average of a group of people
		
	Args:
		persons_list (list): List of people
		current_year (number): The current year

	Returtns:
		age_average (number): The average age of the group of people
	"""
	age_sum = 0
	age_average = 0

	for person in person_list:
		age_sum += person.age(current_year=current_year)

	age_average = age_sum/len(persons_list)

	return age_average

alejandra = Person(first_name="Alejandra", last_name="Rodríguez",birth_year=1992)
miguel = Person(first_name="Miguel", last_name="Rodríguez",birth_year=1993)
claudia = Person(first_name="Claudia", last_name="Rodríguez",birth_year=1987)
raul = Person(first_name="Raul", last_name="Zazueta",birth_year=1963)

person_list = [alejandra, miguel, claudia, raul]

average = average_age(persons_list=person_list, current_year=2020)
