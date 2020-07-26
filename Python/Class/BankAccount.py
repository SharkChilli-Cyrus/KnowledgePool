class BankAccount(object):

    # Constructor
    def __init__(self, accountNumber, accountName, balance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance - amount
    
    def withdraw(self, amount):
        self.balance = self.balance + amount
    
    def info(self):
        text = """
        ===== Bank Account Info =====
        * Account Number: {0}
        * Account Name: {1}
        * Account Balance: {2}
        =============================
        """.format(self.accountNumber, self.accountName, self.balance)
        return text

test_account1 = BankAccount(12345, "Tom", 100.0)
print(test_account1.info())
