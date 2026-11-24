import math


class Account:
    def __init__(self, account_number, owner, pin, balance):
        self.account_number = account_number
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or (isinstance(amount, float) and not math.isfinite(amount))
        ):
            return "Invalid deposit amount."

        if amount <= 0:
            return "Invalid deposit amount."

        self.balance += amount

        return (
            f"Deposit successful.\n"
            f"New balance: ₦{self.balance:,.2f}"
        )

    def withdraw(self, amount):
        if (
            isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or (isinstance(amount, float) and not math.isfinite(amount))
        ):
            return "Invalid withdrawal amount."

        if amount <= 0:
            return "Invalid withdrawal amount."

        if amount > self.balance:
            return (
                f"Insufficient funds.\n"
                f"Balance remains: ₦{self.balance:,.2f}"
            )

        self.balance -= amount

        return (
            f"Withdrawal successful. Please take your cash.\n"
            f"Amount withdrawn: ₦{amount:,.2f}\n"
            f"New balance: ₦{self.balance:,.2f}"
        )
