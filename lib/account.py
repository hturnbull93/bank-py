class Account:
    STARTING_BALANCE = 0
    balance = STARTING_BALANCE
    def deposit(self, amount):
        credit = amount * 100
        self.balance += credit
        displayBalance = self.balance / 100
        displayCredit = credit / 100
        message = "{0:.2f} deposited. Current balance: {1:.2f}"
        return message.format(displayCredit, displayBalance)
