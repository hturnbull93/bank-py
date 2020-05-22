from . import money


class Account:
    STARTING_BALANCE = 0

    def __init__(self):
        self.balance = self.STARTING_BALANCE

    def deposit(self, amount):
        credit = money.pence(amount)
        self.balance += credit
        message = "{0} deposited. Current balance: {1}"
        return message.format(money.pounds(credit), money.pounds(self.balance))

    def withdraw(self, amount):
        debit = money.pence(amount)
        if debit > self.balance:
            return "Insufficient funds"
        self.balance -= debit
        message = "{0} withdrawn. Current balance: {1}"
        return message.format(money.pounds(debit), money.pounds(self.balance))
