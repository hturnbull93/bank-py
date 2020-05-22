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


class TestWithdraw:
    def account_with_one_thousand_deposited(self):
        account = Account()
        account.deposit(1000)
        return account

    def test_pass_100_balance_100_less(self):
        account = self.account_with_one_thousand_deposited()
        result = "100.00 withdrawn. Current balance: 900.00"
        assert account.withdraw(100) == result

    def test_pass_200_balance_200_less(self):
        account = self.account_with_one_thousand_deposited()
        result = "200.00 withdrawn. Current balance: 800.00"
        assert account.withdraw(200) == result

    def test_pass_200_then_100_balance_300_less(self):
        account = self.account_with_one_thousand_deposited()
        account.withdraw(200)
        result = "100.00 withdrawn. Current balance: 700.00"
        assert account.withdraw(100) == result

    def test_over_withdraw_returns_insufficient_funds(self):
        account = self.account_with_one_thousand_deposited()
        result = "Insufficient funds"
        assert account.withdraw(1500) == result

class MockTransaction:
    def __init__(self, credit=None):
        print("MockTransaction.__init__ called with {}".format(credit))

class TestTransactionUse:
    def test_deposit_uses_transaction(self, capfd):
        account = Account(transaction_class=MockTransaction)
        account.deposit(100)
        captured = capfd.readouterr()
        expected_output = "MockTransaction.__init__ called with 10000\n"
        assert captured.out == expected_output
