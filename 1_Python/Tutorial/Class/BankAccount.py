class BankAccount:
    
    # Constructor
    def __init__(self, accountNumber, accountName, balance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def info(self):
        text = """
        ====== BankAccount Info =====
        * Account Number: {0}
        * Account Name: {1}
        * Account Balance: {2}
        =============================
        """.format(self.accountNumber, self.accountName, self.balance)
        return text
    
    def __str__(self):
        return """
        ====== BankAccount Info =====
        * Account Number: {0}
        * Account Name: {1}
        * Account Balance: {2}
        =============================
        """.format(self.accountNumber, self.accountName, self.balance)
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance


test = BankAccount(1, 'Tom', 10000.0)

print(test)
print(test.info())