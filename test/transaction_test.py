from freezegun import freeze_time
import datetime

from lib.transaction import Transaction


class TestDisplay():
    def test_has_date_formatted(self):
        with freeze_time("2020-01-01"):
            transaction = Transaction()
            result = "01/01/2020 || || || "
            assert transaction.display() == result

    def test_has_credit_shown(self):
        with freeze_time("2020-01-01"):
            transaction = Transaction(10000)
            result = "01/01/2020 || 100.00 || || "
            assert transaction.display() == result
