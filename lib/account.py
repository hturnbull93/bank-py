class Account:
    STARTING_BALANCE = 0
    balance = STARTING_BALANCE
    def deposit(self, amount):
        self.balance += amount
        message = "{0}.00 deposited. Current balance: {1}.00"
        return message.format(amount, self.balance)
