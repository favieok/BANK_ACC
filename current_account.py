from Account import Account


class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        super().withdraw(amount)

    def deposit(self, amount):
        super().deposit(amount)

