import datetime


class Transaction:
    date = datetime.datetime.now()
    date_format = date.strftime("%d/%m/%Y")

    def display(self):
        template = "{} || || || "
        return template.format(self.date_format)
