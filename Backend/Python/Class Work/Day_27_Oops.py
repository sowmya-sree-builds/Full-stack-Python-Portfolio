class Account:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = initialBalance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return True
        return False
    def transfer(self, amount, receiverAccount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            receiverAccount.balance = receiverAccount.balance + amount
            return True
        return False
    def showDetails(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder:", self.accountHolder)
        print("Balance:", self.balance)
class Bank:
    def __init__(self, bankName):
        self.bankName = bankName
        self.accounts = []
    def createAccount(self, accountNumber, accountHolder, initialBalance):
        totalAccounts = 0
        for i in self.accounts:
            totalAccounts = totalAccounts + 1
        j = 0
        while j < totalAccounts:
            if self.accounts[j].accountNumber == accountNumber:
                return False
            j = j + 1
        newAcc = Account(accountNumber, accountHolder, initialBalance)
        self.accounts = self.accounts + [newAcc]
        return True
    def findAccount(self, accountNumber):
        totalAccounts = 0
        for i in self.accounts:
            totalAccounts = totalAccounts + 1
        j = 0
        while j < totalAccounts:
            if self.accounts[j].accountNumber == accountNumber:
                return self.accounts[j]
            j = j + 1
        return None
    def showAllAccounts(self):
        totalAccounts = 0
        for i in self.accounts:
            totalAccounts = totalAccounts + 1
        j = 0
        while j < totalAccounts:
            print("-----")
            self.accounts[j].showDetails()
            j = j + 1
bank = Bank("State Bank")
bank.createAccount(101, "Venkat", 5000)
bank.createAccount(102, "Pavan", 8000)
acc1 = bank.findAccount(101)
acc2 = bank.findAccount(102)
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.transfer(1500, acc2)
bank.showAllAccounts()