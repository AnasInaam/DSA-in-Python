from abc import ABC , abstractmethod
class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    def Get_balance(self):
        print(f"This is your Account number: {self.account_number}")
        print(f"This is your Account Holder: {self.account_holder}")
        print(f"This is your Balance: {self.balance}rs/- Only")
        print("-"*30)

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def deposit(self, amount):
        self.balance += amount + (amount * self.interest_rate)
        print(f"Kaha se Churaya: {amount}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Your lost amount is: ", amount)
        else:
            print("Hai kya Paise ju Nikal raha")
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def deposit(self, amount):
        self.balance += amount
        print(f"Kaha se Churaya: {amount}")
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print("Your lost amount is: ", amount)
        else:
            print("Hai kya Paise ju Nikal raha")
def main_menu():
    while True:
        print("1. Create Saving Account")
        print("2. Create Current Account")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account_number = int(input("Enter The Account Number: "))
            account_holder = input("Enter The Account Holder: ")
            balance = float(input("Enter The Balance: "))
            account = SavingAccount(account_number, account_holder, balance)
        elif choice == 2:
            account_number = int(input("Enter The Account Number: "))
            account_holder = input("Enter The Account Holder: ")
            balance = float(input("Enter The Balance: "))
            account = CurrentAccount(account_number, account_holder, balance)
        elif choice == 3:
            break
        else:
            print("Invalid choice")
            continue
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Get Balance")
            print("4. Exit")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif sub_choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif sub_choice == 3:
                account.Get_balance()
            elif sub_choice == 4:
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main_menu()
