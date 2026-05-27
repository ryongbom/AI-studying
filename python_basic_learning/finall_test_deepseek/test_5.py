# Write a simple BankAccount class.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient balance")
        else:
            self.balance -= amount
    def get_balance(self):
        return(self.balance)
    
account = BankAccount("Kim", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())
account.withdraw(2000)