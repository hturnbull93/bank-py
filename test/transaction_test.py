from freezegun import freeze_time
import datetime

with freeze_time("2020-01-01"):
    from lib.transaction import Transaction


class TestDisplay():
    def test_has_date_formatted(self):
        transaction = Transaction()
        result = "01/01/2020 || || || "
        assert transaction.display() == result
