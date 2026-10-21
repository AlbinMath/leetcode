
class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate account numbers
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False

        # Check whether the source account has enough money
        if self.balance[account1 - 1] < money:
            return False

        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False

        # Check sufficient balance
        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True

