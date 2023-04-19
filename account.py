class Account:
    def __init__(self, name: str) -> None:
        """
        Function to setup an account
        :param name: the account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit to account
        :param amount: the amount to deposit
        :return: True if successful, False if not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw from account
        :param amount: the amount to withdraw
        :return: True if successful, False if not
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to return account balance
        :return: account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return account name
        :return: account name
        """
        return self.__account_name
