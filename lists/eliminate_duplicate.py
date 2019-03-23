"""
Given a sorted linked list, delete all duplicates such that each element
appear only once.
"""
def eliminate_duplicates(the_list):
	"""
	Eliminates every duplicate from the list

	Args:
		list: The list of the elements to evaluate

	Returns:
		unique_elements: A list with only the unique elements
	"""
	unique_elements = []
	
	for element in the_list:
		if element not in unique_elements:
			unique_elements.append(element)
	
	return unique_elements