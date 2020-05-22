class Account:
    STARTING_BALANCE = 0
    balance = STARTING_BALANCE
    def deposit(self, amount):
        credit = self.pence(amount)
        self.balance += credit
        message = "{0:.2f} deposited. Current balance: {1:.2f}"
        return message.format(self.pounds(credit), self.pounds(self.balance))

    def pence(self, pounds):
        return pounds * 100

    def pounds(self, pence):
        return pence / 100
