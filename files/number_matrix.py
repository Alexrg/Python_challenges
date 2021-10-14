"""
Give a Comma Separated File (csv) and a column number (zero being the left most
column) return the sum of all entries in that column. Assume that all the
entries in the CSV are numbers. Assume also that there are no column headers.
For example a file looks like this:
1,2,3,4
5,6,7,8
9,10,11,12
the sum of the column 0 will be 1 + 5 + 9 = 15 and the sum of the column 2 will
be 3 + 7 + 11 = 21
"""
import pandas

def extract_matrix_number(file_name):
	"""
	Receives the name's file to open it and exctrat the numbers matrix, to then store it
	in a variable.

	Args:
		file_name (string): The name file

	Returns:
		file_matrix (Pandas object): The number matrix from the file
	"""
	file_matrix = pandas.read_csv(file_name, header=None)

	return file_matrix

def sum_columns():
	"""
	Sums all the columns of a pandas object.

	Returns:
		matrix_number.sum() (Pandas object): The columns added.
	"""
	file_name = "matrix_number.csv"
	matrix_number = extract_matrix_number(file_name)

	return matrix_number.sum()

x = sum_columns()
print(x)
print(type(x))