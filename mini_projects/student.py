from person import Person

class Student():
	def __init__(self, person, password):
		"""
		Initilizes the student's information: their name and password.

		Args:
			person (Object): Instance of the Person Class
			password (string): The stident's password.
		"""
		self.person = person
		self.password = password