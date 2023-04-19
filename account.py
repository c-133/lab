class Account:
    def __init__(self, name: str) -> None:
        """
        Initializes an Account object with a given name and a balance of 0.

        Args:
            name: The name of the account holder.

        Returns:
            None
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposits the specified amount into the account balance.

        Args:
            amount: The amount to be deposited.

        Returns:
            True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the specified amount from the account balance.

        Args:
            amount: The amount to be withdrawn.

        Returns:
            True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Returns the current account balance.

        Args:
            None

        Returns:
            The current account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Returns the name of the account holder.

        Args:
            None

        Returns:
            The name of the account holder.
        """
        return self.__account_name
