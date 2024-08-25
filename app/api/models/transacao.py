from datetime import datetime

class Transaction:
    def __init__(self, type: str, amount: float):
        self.type = type
        self.amount = amount
        self.timestamp = datetime.now()
