from freezegun import freeze_time
import datetime

from lib.account import Account


def xtest_feature():
    account = Account()

    with freeze_time("2012-01-10"):
        account.deposit(1000)

    with freeze_time("2012-01-13"):
        account.deposit(2000)

    with freeze_time("2012-01-14"):
        account.withdraw(500)

    separator = "\n"
    statement = [
        "date || credit || debit || balance ",
        "14/01/2012 || || 500.00 || 2500.00 ",
        "13/01/2012 || 2000.00 || || 3000.00 ",
        "10/01/2012 || 1000.00 || || 1000.00 ",
    ]
    result = separator.join(statement)

    assert account.statement() == result
