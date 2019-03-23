import random 

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

def create_list(length):
	"""
	Creates a list with a length chosen in the argument, that has random
	numbers from 0 to 50

	Args:
		length: The length of the list that will be created

	Returns:
		list: A list with random elements from 0 to 50
	"""
	the_list = []
	
	for element in range(0,length):
		element = random.randint(0, 50)
		the_list.append(element)
	
	return the_list 


print("Enter the length of the list you want to create: ")
list_length = int(input())

the_list = create_list(list_length)

print("Your list: {}".format(the_list))

unique_elements_list = eliminate_duplicates(the_list)
print("Your list with unique elements: {}".format(unique_elements_list))