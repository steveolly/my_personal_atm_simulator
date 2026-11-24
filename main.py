import getpass
from account import Account
from atm import ATM


# ==================================
# PRELOADED CUSTOMER ACCOUNTS
# ==================================

owner_1 = Account(1001, "Ada Obi", 4321, 50000)
owner_2 = Account(1002, "John Doe", 1234, 75000)
owner_3 = Account(1003, "Mary James", 5678, 100000)


# ==================================
# STORE ACCOUNTS IN A DICTIONARY
# ==================================

accounts = {
    owner_1.account_number: owner_1,
    owner_2.account_number: owner_2,
    owner_3.account_number: owner_3
}


# ==================================
# LOGIN FUNCTION
# ==================================

def login(accounts, account_number, pin):

    account = accounts.get(account_number)

    if account is None:
        return "Account not found."

    if account.pin != pin:
        return "Incorrect PIN."

    return account


# ==================================
# ATM MENU
# ==================================

def atm_menu(account):

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":

            balance = account.check_balance()

            print(f"\nYour balance is ₦{balance:,.2f}")

        elif choice == "2":

            try:
                amount = float(input("Enter deposit amount: "))
                print(account.deposit(amount))

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":

            try:
                amount = float(input("Enter withdrawal amount: "))
                print(account.withdraw(amount))

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":

            print(f"\nThank you for banking with us, {account.owner}.")
            print("Please take your card.")

            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# ==================================
# MAIN ATM PROGRAM
# ==================================

def main():

    print("\n================================")
    print("       WELCOME TO OUR ATM       ")
    print("================================")

    while True:

        print()

        try:
            account_number = int(input("Account number: "))

        except ValueError:
            print("Invalid account number.")
            return

        # Ask until the user chooses a valid PIN visibility option
        while True:

            visibility = input("Show PIN while typing? (y/n): ").lower()

            if visibility in ("y", "n"):
                break

            print("Please enter y or n.")

        if visibility == "y":
            pin_input = input("PIN: ")
        else:
            pin_input = getpass.getpass("PIN: ")

        try:
            pin = int(pin_input)

        except ValueError:
            print("Invalid PIN. Please try again.")
            continue

        account = login(accounts, account_number, pin)

        if isinstance(account, Account):

            print(f"\nWelcome, {account.owner}!")

            atm_menu(account)

        else:
            print(f"\nLogin failed: {account}")


# ==================================
# RUN THE PROGRAM
# ==================================

if __name__ == "__main__":
    main()