class BankAccount(object):

    # Constructor
    def __init__(self, accountNumber, accountName, balance):
        self.accountName = accountNumber
        self.accountName = accountName
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance - amount
    
    def withdraw(self, amount):
        self.balance = self.balance + amount
    

test_account1 = BankAccount(12345, "Tom", 100.0)
print(test_account1.accountName)
