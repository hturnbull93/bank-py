class TestDeposit:
    def test_pass_100_balance_100(self):
        account = Account()
        result = "100.00 deposited. Current balance: 100.00"
        assert account.deposit(100) == result