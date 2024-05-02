import random
class Bank:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.admin_password = "123"
        self.admin_name = "admin"
        self.loan_feature = True
        self.total_balance = 0
        self.total_loan_amount = 0
        self.is_bankrupt = False

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100, 999)
        while account_number in self.users: # For the uniqueness of each account number
            account_number = random.randint(100, 999)
        self.users[account_number] = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "balance": 0,
            "loan_taken": 0,
            "loan_remaining": 0,
            "transaction_history": []
        }
        print("Your account has been created successfully.")
        print(f"Here's your Account Number: {account_number}\n")

    def deposit(self, account_number, amount):
        if account_number not in self.users:
            print("Account does not exist\n")
            return
        self.users[account_number]["balance"] += amount
        self.total_balance += amount
        self.users[account_number]["transaction_history"].append(f"Deposited: {amount}")
        print(f"You've deposited: {amount} successfully!!\n")

    def withdraw(self, account_number, amount):
        if account_number not in self.users:
            print("Account does not exist\n")
            return
        if amount > self.users[account_number]["balance"]:
            print("Withdrawal amount exceeded!!\n")
            return
        self.users[account_number]["balance"] -= amount
        self.total_balance -= amount
        self.users[account_number]["transaction_history"].append(f"Withdrew: {amount}")
        print(f"You've withdrawn: {amount} successfully!!\n")

    def check_balance(self, account_number):
        if account_number not in self.users:
            print("Account does not exist\n")
            return
        bal = self.users[account_number]["balance"]
        print(f"Your balance: {bal}\n")

    def take_loan(self, account_number, amount):
        if account_number not in self.users:
            print("Account does not exist!!\n")
            return
        if self.loan_feature and self.users[account_number]["loan_taken"] <= 2:
            self.users[account_number]["loan_taken"] += 1
            self.users[account_number]["loan_remaining"] += amount
            self.users[account_number]["balance"] += amount
            self.total_loan_amount += amount
            self.users[account_number]["transaction_history"].append(f"Took a loan of {amount}")
            print(f"Loan of {amount} granted\n")
        else:
            print("Loan feature currently not available or maximum limit reached\n")

    def transfer(self, sender_account_number, receiver_account_number, amount):
        if sender_account_number not in self.users or receiver_account_number not in self.users:
            print("Invalid account number!!\n")
            return
        if amount > self.users[sender_account_number]["balance"]:
            print("Insufficient funds!!\n")
            return
        self.users[sender_account_number]["balance"] -= amount
        self.users[receiver_account_number]["balance"] += amount
        self.users[sender_account_number]["transaction_history"].append(f"Transferred {amount} to {self.users[receiver_account_number]['name']}")
        self.users[receiver_account_number]["transaction_history"].append(f"Received {amount} from {self.users[sender_account_number]['name']}")
        print(f"You've Transferred {amount} successfully!!\n")

    def check_transaction_history(self, account_number):
        if account_number not in self.users:
            print("Account does not exist")
            return
        transactions = self.users[account_number]["transaction_history"]
        print(*transactions, sep='\n')
        print()

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        account_number = self.bank.create_account(name, email, address, account_type)
        print("The account has been created successfully.")
        print(f"Here's The Account Number: {account_number}\n")

    def delete_account(self, account_number):
        if account_number not in self.bank.users:
            print("Account does not exist")
            return
        del self.bank.users[account_number]
        print("The account has been deleted successfully.\n")

    def list_accounts(self):
        for acc_num, person_info in self.bank.users.items():
            for key in person_info:
                print(f"\t{key} : {person_info[key]}")
            print("\n")

    def check_total_balance(self):
        print(f"The total balance is: {self.bank.total_balance}\n")

    def check_total_loan_amount(self):
        print(f"The total loan is: {self.bank.total_loan_amount}\n")

    def toggle_loan_feature(self):
        self.bank.loan_feature = not self.bank.loan_feature
        print("Loan feature turned " + ("off" if not self.bank.loan_feature else "on") + "\n")


IBBL = Bank("Islami Bank Bangladesh Limited")
admin = Admin(IBBL)

while True:
    print("Welcome to Islami Bank Bangladesh Limited !!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("1. Create an Account")
            print("2. Deposit balance")
            print("3. Withdraw balance")
            print("4. Check available balance")
            print("5. Check transaction history")
            print("6. Take loan")
            print("7. Transfer balance")
            print("8. Logout")
            op = input("Enter your choice: ")

            if op == '1':
                name = input("Your name: ")
                email = input("Your email: ")
                address = input("Your address: ")
                account_type = input("Your account type (Savings/Current): ")
                IBBL.create_account(name, email, address, account_type)
            elif op == '2':
                if IBBL.is_bankrupt == False:
                    account_number = int(input("Your account number: "))
                    amount = int(input("The amount you want to deposit: "))
                    IBBL.deposit(account_number, amount)
                else: 
                    print("The bank went bankrupt!!")
            elif op == '3':
                account_number = int(input("Your account number: "))
                amount = int(input("The amount you want to withdraw: "))
                IBBL.withdraw(account_number, amount)
            elif op == '4':
                account_number = int(input("Your account number: "))
                IBBL.check_balance(account_number)
            elif op == '5':
                account_number = int(input("Your account number: "))
                IBBL.check_transaction_history(account_number)
            elif op == '6':
                account_number = int(input("Your account number: "))
                amount = int(input("The amount of loan: "))
                IBBL.take_loan(account_number, amount)
            elif op == '7':
                sender_account_number = int(input("Your account number: "))
                receiver_account_number = int(input("The account number you want to transfer balance: "))
                amount = int(input("The amount you want to transfer: "))
                IBBL.transfer(sender_account_number, receiver_account_number, amount)
            elif op == '8':
                break
            else:
                print("Invalid choice")
    elif choice == '2':
        na = input("Enter your name: ")
        pas = input("Enter the password: ")
        if na == IBBL.admin_name and pas == IBBL.admin_password:
            while True:
                print("1. Create an Account")
                print("2. Delete an Account")
                print("3. View All Users' Accounts")
                print("4. Check Bank's available balance")
                print("5. Check Bank's total loan Amount")
                print("6. Turn the loan feature On/Off")
                print("7. Logout")
                op = input("Enter your choice: ")

                if op == '1':
                    name = input("Your name: ")
                    email = input("Your email: ")
                    address = input("Your address: ")
                    account_type = input("Your account type (Savings/Current): ")
                    IBBL.create_account(name, email, address, account_type)
                elif op == '2':
                    account_number = int(input("Account number: "))
                    admin.delete_account(account_number)
                elif op == '3':
                    admin.list_accounts()
                elif op == '4':
                    admin.check_total_balance()
                elif op == '5':
                    admin.check_total_loan_amount()
                elif op == '6':
                    admin.toggle_loan_feature()
                elif op == '7':
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid name or password")
    elif choice == '3':
        break
    else:
        print("Invalid Choice")
