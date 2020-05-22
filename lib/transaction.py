import datetime

from .money import pounds


class Transaction:
    def __init__(self, credit=None, debit=None, balance=None):
        self.DATE = datetime.datetime.now()
        self.DATE_FORMAT = self.DATE.strftime("%d/%m/%Y ")
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def display(self):
        separator = "|| "
        items = [
            self.DATE_FORMAT, 
            self.__render(self.credit), 
            self.__render(self.debit), 
            self.__render(self.balance)
        ]
        return separator.join(items)

    def __render(self, item):
        if item is not None:
            template = "{} "
            return template.format(pounds(item))
        return ""
