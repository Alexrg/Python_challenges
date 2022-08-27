"""
Online Shopping

In this exercise, you'll start designing models for an online shopping service. Concretely, you'll need to build three classes:

    A User will have an id and a name, and be able to sell_product, buy_product, and write_review.
    A Product will contain a name, a description, a seller, a collection of reviews, a price, and an availability.
    A Review will contain a description, a user (who wrote the review), and a product (for which the review is written)

Each of these classes should be nicely printable.

By the time you're done, the following lines of code should be valid:

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True

"""
class User():
    def __init__(self, user_id, user_name):
        """
        The User class stores the id, name and their given reviews.
        
        Args:
            user_id (int): User's identification number.
            user_name (string): User's first name.
        """
        self.user_id = user_id
        self.user_name = user_name
        self.reviews = []

    def __str__(self):
        """
        Print the user data: name and id. Made for debugging purposes.
        
        Returns:
            (string): User data in a readable format.
        """
        return "User name: {}".format(self.user_name)

    def sell_product(self,product_name,product_description,price):
        """
        Print the user data: name and id. Made for debugging purposes.
        
        Args:
            product_name (string): The name of the product that will be sell.
            product_description (string): The description of the product
            that will be sell.
            price (int): The price of the product that will be sell.
        
        Returns:
            product_to_sel (object): An instance of the product class.
        """
        product_to_sell = Product(product_name,product_description,price)
        product_to_sell.available = True
        
        return product_to_sell

    def buy_product(self, product):
        """
        Changes the availability of the product to False when bougth.
        """
        product.available = False