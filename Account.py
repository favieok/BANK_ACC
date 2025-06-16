class Account:
    def __init__(self,balance):
        self.balance = balance
        #print("Account balance is:",self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(self.balance)


#user = Account(40000)

#user.withdraw(20000)
#user.deposit(5000)




