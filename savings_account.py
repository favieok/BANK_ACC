from Account import Account

class SavingsAccount(Account):
    def __init__(self,balance):
        Account.__init__(self, balance)

    def withdraw(self,amount):
        if amount <= 10000:
            return super().withdraw(amount)

        else:
            print("Oops!You've exceeded your limit")


    def deposit(self,amount):
        return super().deposit(amount)





