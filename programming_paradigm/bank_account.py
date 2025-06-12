class BankAccount:
    def __init__(self, initial_balance=0):
        self.initial_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.initial_balance  += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.initial_balance:
            return False
        self.initial_balance -= amount
        return True
        
    def display_balance(self):
        print(f"Current balance: {self.initial_balance}")