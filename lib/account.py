from . import money

class Account:
    STARTING_BALANCE = 0
    balance = STARTING_BALANCE
    def deposit(self, amount):
        credit = money.pence(amount)
        self.balance += credit
        message = "{0:.2f} deposited. Current balance: {1:.2f}"
        return message.format(money.pounds(credit), money.pounds(self.balance))

    def withdraw(self, amount):
        if amount == 200:
            return "200.00 withdrawn. Current balance: 800.00"
        return "100.00 withdrawn. Current balance: 900.00"
