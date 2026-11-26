from account import Account

class ATM:
    def __init__(self,accounts):
        self.accounts = accounts
        self.current_account = None

    def login(self,account_number,PIN):
        account = self.accounts.get(account_number)

        if account is None:
            return "Account not found."
        elif account.is_blocked:
            return "This account has been blocked"
        elif account.pin != PIN:
            account.failed_attempts += 1
            print(f"Incorrect PIN, you have {3-account.failed_attempts} attempt left")
            if account.failed_attempts >= 3:
                account.is_blocked = True
                return "This account has been blocked"
            
        account.failed_attempts = 0
        self.current_account = account

        return account
        