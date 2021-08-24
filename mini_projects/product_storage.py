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
	try:
		created_product = Product(name=input("Enter product: "),
								price=int(input("Enter product price: ")))
	except ValueError:
		print("You entered a wrong value for the product price")

	return created_product

def add_products():
	"""
	Adds the created instances of the product made by the user.

	Returns:
		products_tuple (tuple): A tuple containing all the objects created by the user.
	"""
	add_more = 0
	products_tuple = ()
	
	while add_more == 0:
		products_tuple += (create_product(),)

		add_more = int(input("More products? yes (0), no (1): "))
	
	return products_tuple

def print_products(products_tuple):
	"""
	Prints in screen all the products and it's prices.
	"""
	for element in products_tuple:
		print("Product: {} Price: {}".format(element.name, element.price))

	return None

products = add_products()
print_products(products)

