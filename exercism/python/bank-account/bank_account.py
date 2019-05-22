import threading
lock = threading.Lock()

class BankAccount(object):
    def __init__(self):
        self.status = 'closed'

    def get_balance(self):
        if self.status == 'open':
            return self.balance
        else:
            raise ValueError('Balance unavailable. Account is closed')

    def open(self):
        if self.status == 'closed':
            self.status = 'open'
            self.balance = 0
        else:
            raise ValueError('Account already open.')

    def deposit(self, amount):
        if self.status == 'open':
            if amount >= 0:
                with lock:
                    self.balance += amount
            else:
                raise ValueError('Cannot deposit a negative amount.')
        else:
            raise ValueError('Cannot deposit. Account is closed.')

    def withdraw(self, amount):
        if self.status == 'open':
            if amount >= 0:
                if self.balance - amount >= 0:
                    with lock:
                        self.balance -= amount
                else:
                    raise ValueError('Insufficient funds.')
            else:
                raise ValueError('Cannot withdraw a negative amount.')
        else:
            raise ValueError('Cannot withdraw. Account is closed.')

    def close(self):
        if self.status == 'open':
            self.status = 'closed'
        else:
            raise ValueError('Account is already closed.')

