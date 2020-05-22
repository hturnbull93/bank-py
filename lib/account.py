from . import money

from .transaction import Transaction


class Account:
    STARTING_BALANCE = 0
    STATEMENT_HEADER = "date || credit || debit || balance \n"

    def __init__(self, transaction_class=Transaction):
        self.balance = self.STARTING_BALANCE
        self.TRANSACTION_CLASS = transaction_class
        self.TRANSACTION_HISTORY = []

    def deposit(self, amount):
        credit = money.pence(amount)
        self.balance += credit
        self.__add_transaction(credit=credit, balance=self.balance)
        message = "{0} deposited. Current balance: {1}"
        return message.format(money.pounds(credit), money.pounds(self.balance))

    def withdraw(self, amount):
        debit = money.pence(amount)
        if debit > self.balance:
            return "Insufficient funds"
        self.balance -= debit
        self.__add_transaction(debit=debit, balance=self.balance)
        message = "{0} withdrawn. Current balance: {1}"
        return message.format(money.pounds(debit), money.pounds(self.balance))

    def statement(self):
        REVERSE_TRANSACTIONS = self.__reverse_transactions()
        MAPPED_ROWS = map(self.__transaction_mapping, REVERSE_TRANSACTIONS)
        SEPARATOR = "\n"
        JOINED_ROWS = SEPARATOR.join(MAPPED_ROWS)
        return self.STATEMENT_HEADER + JOINED_ROWS

    def __add_transaction(self, credit=None, debit=None, balance=None):
        transaction = self.TRANSACTION_CLASS(credit, debit, balance)
        self.TRANSACTION_HISTORY.append(transaction)

    def __reverse_transactions(self):
        REVERSE_TRANSACTIONS = self.TRANSACTION_HISTORY.copy()
        REVERSE_TRANSACTIONS.reverse()
        return REVERSE_TRANSACTIONS

    def __transaction_mapping(self, transaction):
        return transaction.display()
