import datetime


class Transaction:
    def __init__(self):
        self.DATE = datetime.datetime.now()
        self.DATE_FORMAT = self.DATE.strftime("%d/%m/%Y")

    def display(self):
        template = "{} || || || "
        return template.format(self.DATE_FORMAT)
