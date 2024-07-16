class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance is ₹{self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance is ₹{self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        print(f"Current balance is ₹{self.balance}.")
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ₹{interest}. New balance is ₹{self.balance}.")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance is ₹{self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")


# Create a savings account
savings = SavingsAccount("SA123", balance=1000, interest_rate=0.02)
savings.get_balance()
savings.deposit(200)
savings.withdraw(150)
savings.apply_interest()

# Create a checking account
checking = CheckingAccount("CA123", balance=500, overdraft_limit=200)
checking.get_balance()
checking.deposit(300)
checking.withdraw(900)
checking.withdraw(200)
checking.get_balance()
