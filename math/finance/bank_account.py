class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount
        return self.initial_balance 

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal 
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """

    def get_balance(self):
        """Returns the current balance in the account."""

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""