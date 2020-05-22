from . import money

from .transaction import Transaction


class Account:
    STARTING_BALANCE = 0

    def __init__(self, transaction_class=Transaction):
        self.balance = self.STARTING_BALANCE
        self.TRANSACTION_CLASS = transaction_class

    def deposit(self, amount):
        credit = money.pence(amount)
        self.balance += credit
        transaction = self.__add_transaction(credit=credit, balance=self.balance)
        message = "{0} deposited. Current balance: {1}"
        return message.format(money.pounds(credit), money.pounds(self.balance))

    def withdraw(self, amount):
        debit = money.pence(amount)
        if debit > self.balance:
            return "Insufficient funds"
        self.balance -= debit
        transaction = self.__add_transaction(debit=debit, balance=self.balance)
        message = "{0} withdrawn. Current balance: {1}"
        return message.format(money.pounds(debit), money.pounds(self.balance))

    def __add_transaction(self, credit=None, debit=None, balance=None):
        return self.TRANSACTION_CLASS(credit, debit, balance)
