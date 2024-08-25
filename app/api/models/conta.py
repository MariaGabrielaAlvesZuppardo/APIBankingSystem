from datetime import datetime
from typing import List, Tuple

class Account:
    sequential_account_number = 1

    def __init__(self, client: 'Client', initial_balance: float):
        self.branch = "0001"
        self.number = Account.sequential_account_number
        Account.sequential_account_number += 1
        self.client = client
        self.balance = initial_balance
        self.history: List[Tuple[datetime, str, float]] = []
        self.daily_transactions = {}

    def deposit(self, amount: float):
        self.balance += amount
        self.history.append((datetime.now(), "Deposit", amount))

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append((datetime.now(), "Withdrawal", amount))
        else:
            raise ValueError("Insufficient balance")

    def view_statement(self):
        return [(date, type, amount) for date, type, amount in self.history]
