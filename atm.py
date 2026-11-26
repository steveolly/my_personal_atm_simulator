from account import Account

class ATM:
    def __init__(self,accounts):
        self.accounts = accounts
        self.current_account = None

    def login(self,account_number,PIN):
        account = self.accounts.get(account_number)

        if account is None:
            return "Account not found."
        elif account.pin != PIN:
            return "Incorrect PIN."

        self.current_account = account

        return account
        