"""
Imagine you're a teacher who needs to send a message to each of your students
reminding them of their missing assignments and grade in the class. You have
each of their names, number of missing assignments, and grades on a spreadsheet
and just have to insert them into placeholders in a message you came up with.
"""
class ListConverter():
	"""
	Converts the receibed string to a list of either strings or numbers.

	Args:
		input_string (string): A large string that was entered by the user.
	"""
	def __init__(self, input_string):
		self.input_string = input_string

	def string_list(self):
		"""
		Converts the receibed string to a list of names.

		Returns:
			(list): A list containing the student's names.
		"""
		return self.input_string.split(',')

	def number_list(self):
		"""
		Converts the receibed string to a list of numbers.

		Returns:
			(list): A list containing the student's data (grades or assignment number).
		"""
		number_list = self.string_list()

		for index, element in enumerate(number_list):
			try:
				number_list[index] = int(element)
			except ValueError:
				print("The value entered was not a number")
				break

		return number_list


names = input('Enter names separeted by commas: ')
assignments = input('Enter the number of assignments separeted by commas: ')
grades = input('Enter grades separeted by commas: ')

students = {}

names_list = ListConverter(names).string_list()
assignments_list = ListConverter(assignments).number_list()
grades_list = ListConverter(grades).number_list()

print("names: {} ".format(names_list))
print("grades: {} ".format(assignments_list))
print("grades: {} ".format(grades_list))

for index, name in enumerate(names_list):
	students[name] = {'Assignments':assignments_list[index],'Grade':grades_list[index]}

print(students)

for student in students.keys():
	message = "Hi {},\n\nThis is a reminder that you have {} assignments left to\
	submit before you can graduate. You're current grade is {} and can increase to\
	{} if you submit all assignments before the due date.\n\n".format(student,
		students[student].get('Assignments'),students[student].get('Grade'),
		students[student].get('Grade')+10)
	
	print(message)
