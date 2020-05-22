import datetime

from .money import pounds


class Transaction:
    def __init__(self, credit=None, debit=None):
        self.DATE = datetime.datetime.now()
        self.DATE_FORMAT = self.DATE.strftime("%d/%m/%Y")
        self.credit = credit
        self.debit = debit

    def display(self):
        template = "{} || {}|| {}|| "
        return template.format(self.DATE_FORMAT, self.format(self.credit), self.format(self.debit))

    def format(self, item):
        if item is not None:
            template = "{:.2f} "
            return template.format(pounds(item))
        return ""
