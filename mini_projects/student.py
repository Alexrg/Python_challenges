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

	def get_name(self):
		"""
		Returns the full name os the student.
		
		Returns:
			student_name (string): Student's full name
		"""
		student_name = self.person.full_name()
		return 


alejandra = Person(first_name="Alejandra", last_name="Rodríguez",birth_year=1992)
student_alejandra = Student(person=alejandra,password="123456")