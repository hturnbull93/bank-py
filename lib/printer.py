class Printer:
    STATEMENT_HEADER = "date || credit || debit || balance \n"

    def print_statement(self, transactions):
        SEPARATOR = "\n"
        JOINED_ROWS = SEPARATOR.join(transactions)
        print (self.STATEMENT_HEADER + JOINED_ROWS)

