
class Bank:
    def __init__(self):

        self.name = ''
        self.address = ''
        self.age = ''
        self.balance = ''
        self.menu()

    def menu(self):
        user_input = input('''
                           1. Enter 1 to check_details
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance 
                           ''')
        if user_input == '1':
            self.check_detail()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("Try")

    def check_detail(self):
        self.name = input("Enter your name")
        self.address = input("Enter your address")
        self.age = input("Enter your age")
        self.amount = self.balance
        print("Details added successfully")
        print("Your Details is")
        self.menu()

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit successfully")
        else:
            print("Invalid pin")
        self.menu()

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient funds")
        else:
            print("Enter a valid pin")
        self.menu()

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
        self.menu()
