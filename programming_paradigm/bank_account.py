class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if amount < 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return "Insufficient funds."
            
        
    def display_balance(self):
        return f"current amount: ${self.account_balance}"
