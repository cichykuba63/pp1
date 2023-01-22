import random

class Bank:
    def __init__(self):
        self.account_no = random.randint(10_000_000_000_000_000_000_000_000, 99_999_999_999_999_999_999_999_999)
        self.balance = 0