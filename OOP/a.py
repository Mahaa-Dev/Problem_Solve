class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
    def get_balance(self):
        return self.__balance

# create a new bank account with a balance of $1000
account = BankAccount(1000)

# deposit $500
account.deposit(500)

# withdraw $200
account.withdraw(200)

# check the balance
print(account.get_balance()) # 1300

