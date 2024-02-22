class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with an initial balance of ${initial_balance}")
        else:
            print("Account already exists. Please choose a different account number.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Account {account_number} balance: ${balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} into account {account_number}. New balance: ${self.accounts[account_number]}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                print(f"Withdrew ${amount} from account {account_number}. New balance: ${self.accounts[account_number]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Display Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, initial_balance)
        elif choice == '2':
            account_number = input("Enter account number: ")
            bank.display_balance(account_number)
        elif choice == '3':
            account_number = input("Enter account number: ")
            deposit_amount = float(input("Enter the amount to deposit: "))
            bank.deposit(account_number, deposit_amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw(account_number, withdraw_amount)
        elif choice == '5':
            print("Thank you for using the Banking System. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
