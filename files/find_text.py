"""
Write a function that a phrase and a text file as inputs. The function returns
True if the phrase is found in the document and returns False otherwise. Note:
Newline characters will not be included in the phrase.
"""
def extract_text_from_file(file_name):
	"""
	Receives the name's file to open it and exctrat the text, to then store it
	in a variable.

	Args:
		file_name (string): The name file

	Returns:
		file_text (string): The text from the file
	"""
	file =  open(file_name, mode="r")
	file_text = file.read()
	file.close()

	return file_text


file_name = 'donquijote_capitulouno.txt'

print(extract_text_from_file(file_name=file_name))