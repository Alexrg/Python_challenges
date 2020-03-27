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
		self.student_projects = []

	def get_name(self):
		"""
		Returns the full name os the student.
		
		Returns:
			student_name (string): Student's full name
		"""
		student_name = self.person.full_name()
		return student_name

	def check_password(self, password):
		"""
		Check if the student's given password was the created password.

		Returns:
			check (boolean): A truth value depending on the comparission.
		"""
		check = self.password == password
		return check

	def add_projects(self, project_name):
		"""
		Add the given project to the student's projects.

		Returns:
			self.student_projects (list): A list of the student's projects.
		"""
		self.student_projects.append(project_name)
		return self.student_projects


alejandra = Person(first_name="Alejandra", last_name="Rodríguez",birth_year=1992)
student_alejandra = Student(person=alejandra,password="123456")
print(student_alejandra.check_password("123456"))
print(student_alejandra.add_projects("Blackjack Minigame"))
print(student_alejandra.add_projects("Memory Minigame"))
print(student_alejandra.student_projects)
