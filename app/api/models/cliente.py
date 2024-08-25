from datetime import datetime
from typing import List

class Client:
    def __init__(self, name: str, birth_date: datetime, cpf: str, address: str):
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.cpf = cpf
        self.accounts: List['Account'] = []

    def add_account(self, account: 'Account'):
        self.accounts.append(account)
