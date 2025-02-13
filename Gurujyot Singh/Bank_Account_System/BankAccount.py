import json
import os
import datetime

class BankAccount:
    def __init__(self, accno, holder_name):        # Call The Parameterized Constructor

        #  Declaring variable to be used globally in class

        self.accno = accno
        self.holder_name = holder_name
        self.balance = 0
        self.transactions = []
        self.f = f"accounts/{self.accno}.json"   # Creates file by account number
        self.load_account()           # loads the detail if account already exist

    # Calling this method when user choose to deposit cash (i.e 2.1)
    def money_deposit(self, amount):        # Getting value from the user and passing it through function
        if amount > 0:
            self.balance += amount      # adds amount to balance
            self.transactions.append(f"{datetime.datetime.now()} - Deposited: Rs. {amount}") # adds the transaction in list with date and time
            self.save_detail()  # used to save details of the above-mentioned values
            print("Your account is credited by Rs. ",amount,"\nYour current balance: Rs. ",self.balance)
        else:
            print("Please enter a valid value.")

    # Calling this method when user choose to withdraw cash (i.e 2.2)
    def money_withdraw(self, amount):  # Getting value from the user and passing it through function
        if amount > 0 and amount <= self.balance:   # checks entered amount is greater than 0 and less than balance
            self.balance -= amount  # deducts amount to balance
            self.transactions.append(f"{datetime.datetime.now()} - Withdrawn: Rs. {amount}")  # adds the transaction in list with date and time
            self.save_detail() # used to save details of the above-mentioned values
            print("Your account is debited by Rs. ",amount,"\nYour current balance: Rs. ",self.balance)
        else:
            print("You don't have enough Balance or invalid amount.")

    # Calling this method when user choose to check Balance (i.e 2.3)
    def check_balance(self):       # checks the balance
        print("Account Number: ",self.accno,"\nHolder Name: ",self.holder_name,"\nCurrent Balance: Rs.,",self.balance)

    # Calling this method when user choose check Transaction Histroy  (i.e 2.4)
    def history(self):  # checks the history by using self.transaction var
        print(f"Transaction History for {self.holder_name} ({self.accno}):")
        for transaction in self.transactions:
            print(transaction)

    def save_detail(self):  # saves the data to the file
        data = {
            "Account Number": self.accno,
            "Holder Name": self.holder_name,
            "Balance": self.balance,
            "Transactions": self.transactions
        }
        with open(self.f, "w") as file:  # Updates the data in file and Creates file by acc no if not existed
            json.dump(data, file, indent=4)


    def load_account(self):     # loads the data by opening acc no file
        if os.path.exists(self.f):
            with open(self.f, "r") as file:  # opening in read mode
                data = json.load(file)
                self.balance = data.get("Balance", 0)  # fetching balance and transaction value
                self.transactions = data.get("Transactions", [])

# Calling this method when user choose to Create New Account cash (i.e 1)
def create_account():      # creates new account for user
    os.makedirs("accounts", exist_ok=True)

    accno = input("Enter Account Number (10 digits): ") # user input
    if not accno.isdigit() or len(accno) != 10:       # checks the length of acc no and checks wheter value is in digit or not
        print("Invalid account number...Add numbers upto 10 digits .")
    else:
        f = f"accounts/{accno}.json"        # creates file
        if os.path.exists(f):
            print("This Account No. already exists.")
        else:
            holder_name = input("Enter Account Holder Name: ")
            account = BankAccount(accno, holder_name)      # giving value to constructor by calling obj
            account.save_detail()   # used for saving file details
            print("Account created successfully!")
            return account


# Calling this method when user choose to Access Existing Acount (i.e 2)
def check_account():
    accno = input("Enter Account Number: ")    #user input
    if not accno.isdigit() or len(accno) != 10:  # checks the length of acc no and checks wheter value is in digit or not
        print("Invalid account number...Add numbers upto 10 digits .")
    else:
        f = f"accounts/{accno}.json"
        if os.path.exists(f):
            with open(f, "r") as file:
                data = json.load(file)
                holder_name = data.get("Holder Name")  # fetching the holder name from file
                account = BankAccount(accno, holder_name)  # giving value to constructor by calling obj

            while True:
                    print("\n WELCOME",holder_name.upper())     # to display username in Upper case

                    # Selection Options for the user to perform particular task after selecting choice 2 ( Access Acc)

                    print("\nSelect an option:")
                    print("1. Deposit money \t 2. Withdraw money")
                    print("3. Check Balance \t 4. View Transaction History")
                    print("5. Create New Acc \t 6. Exit")

                    choice = input("\nEnter your choice: ")
                    if choice == "1":
                        amt = int(input("Enter amount to deposit: "))
                        account.money_deposit(amt)
                    elif choice == "2":
                        amt = int(input("Enter amount to withdraw: "))
                        account.money_withdraw(amt)
                    elif choice == "3":
                        account.check_balance()
                    elif choice == "4":
                        account.history()
                    elif choice == "5":
                        create_account()
                    elif choice == "6":
                        print("Exiting... Thank you!")      # by selecting this while loop comes to an end
                        break
                    else:
                        print("Invalid choice. Please try again.")
        else:
            print("Account not found. Do you want to create a new account?")       # if user doesn't have account but still trying to access existing acc
            if input("Yes or No: ").lower() == "yes":
                create_account()


# Selection Options for the user to perform particular task

print(" Select an option : ")
print("1. Create New Account")
print("2. Access Existing Account")
choice = input("Enter your choice: ")
if choice == "1":
    create_account()
elif choice == "2":
    check_account()
else:
    print("Invalid choice. Exiting...")
