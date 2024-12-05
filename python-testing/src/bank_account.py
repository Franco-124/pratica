from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError


class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, ammount):
        if ammount < 0:
            raise ValueError("Deposit amount must be positive")
        if ammount > 0:
            self.balance += ammount
            self._log_transaction(f"Deposited {ammount}. New balance: {self.balance}")
        
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.weekday() in (5, 6):  # 5 = Sábado, 6 = Domingo
            raise WithdrawalTimeRestrictionError("Withdrawals are not allowed on weekends")

        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")

        if amount > self.balance:
            raise InsufficientFundsError(f"Withdrawal of {amount} exceeds balance {self.balance}")

        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance