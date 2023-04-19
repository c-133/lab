from account import Account

class TestAccount:

    def setup_method(self):
        # Create an instance of Account before each test method
        self.account = Account("John")

    def test_init(self):
        assert self.account.get_name() == "John"
        assert self.account.get_balance() == 0

    def test_deposit(self):
        assert self.account.deposit(-100) is False
        assert self.account.deposit(0) is False
        assert self.account.deposit(50) is True
        assert self.account.get_balance() == 50

    def test_withdraw(self):
        assert self.account.withdraw(-100) is False
        assert self.account.withdraw(0) is False
        assert self.account.withdraw(100) is False
        assert self.account.withdraw(20) is True
        assert self.account.get_balance() == 0
