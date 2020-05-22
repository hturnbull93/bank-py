from lib.account import Account


class TestDeposit:
    def test_pass_100_balance_100(self):
        account = Account()
        result = "100.00 deposited. Current balance: 100.00"
        assert account.deposit(100) == result

    def test_pass_200_balance_200(self):
        account = Account()
        result = "200.00 deposited. Current balance: 200.00"
        assert account.deposit(200) == result

    def test_pass_200_then_100_balance_300(self):
        account = Account()
        account.deposit(200)
        result = "100.00 deposited. Current balance: 300.00"
        assert account.deposit(100) == result

    def test_pass_10_50_balance_10_50(self):
        account = Account()
        result = "10.50 deposited. Current balance: 10.50"
        assert account.deposit(10.50) == result
