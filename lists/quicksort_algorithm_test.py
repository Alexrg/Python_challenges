import unittest
from quicksort_algorithm import create_list


class TestCreateListMethod(unittest.TestCase):

	def test_number_of_elements(self):
		"""
		Test if the number of elements created in the create_list method is correct.
		"""
		
		list_elements = len(create_list())

		self.assertEqual(list_elements, 10)


if __name__ == '__main__':
    unittest.main()