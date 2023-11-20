class ATM:
    def __init__(self):     # Constructor
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, How would you like to proceed?
        1. Enter 1 to create the pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check Balance
        5. Enter 5 to Exit.
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Exit")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")

        self.menu()


    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")

            self.menu()

    def withdraw(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successfull")
            else:
                print("insufficient funds")
        else:
            print("Invalid pin")

            self.menu()

    def check_balance(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")

            self.menu()




# output in the console shown as below:

# from main import ATM
# sbi = ATM()
#         Hello, How would you like to proceed?
#         1. Enter 1 to create the pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to check Balance
#         5. Enter 5 to Exit.
#         >? 1
# Enter your pin>? 1234
# Pin set successfully
# sbi.deposit()
# Enter your pin>? 1234
# Enter the amount>? 8000
# Deposit Successfully
# sbi.withdraw()
# Enter the pin>? 1234
# Enter the amount>? 5000
# Operation Successfull
# sbi.check_balance()
# Enter the pin>? 1234
# 3000
# 5
# 5
# 5
# 5
# sbi = ATM()
#         Hello, How would you like to proceed?
#         1. Enter 1 to create the pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to check Balance
#         5. Enter 5 to Exit.
#         >? 1
# Enter your pin>? 1234
# Pin set successfully

