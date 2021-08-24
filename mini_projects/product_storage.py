"""
Create a program that stores product information, as an object, when filing the
product, you must ask if one more is added, the products will be stored as a
tuple of objects, in the end all products will be traversed and printed
on screen.

1. The amount of features to add is free.
2. Must be only one file.
3. PEP 8 must be used.
"""
class Product(object):
	"""
	Object class of a product. Stores the name and price.
	"""
	name = ""
	price = 0.0

	def __init__(self, name, price):
		self.name = name
		self.price = price

def create_product():
	"""
	Creates an instance of the product object.

	Returns:
		created_product (object): The product object instance.
	"""
	created_product = Product(name=input("Enter product: "), 
							price=int(input("Enter product price: ")))
	print(type(created_product))
	return created_product