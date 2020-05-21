class Account:
    def deposit(self, amount):
        message = "{0}.00 deposited. Current balance: {0}.00"
        return message.format(amount)
