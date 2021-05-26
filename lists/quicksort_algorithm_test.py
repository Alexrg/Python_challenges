import unittest
from quicksort_algorithm import create_list


<<<<<<< HEAD
class TestCreateListMethod(unittest.TestCase):
=======
class TestStringMethods(unittest.TestCase):
>>>>>>> 87f1d17806e8b10b341dbb7f95a97179aadf08d5

	def test_number_of_elements(self):
		"""
		Test if the number of elements created in the create_list method is correct.
		"""
		
		list_elements = len(create_list())

		self.assertEqual(list_elements, 10)

<<<<<<< HEAD

=======
>>>>>>> 87f1d17806e8b10b341dbb7f95a97179aadf08d5
if __name__ == '__main__':
    unittest.main()