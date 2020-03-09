class BankAccount:
    """A class example in python that models a bank account"""
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        self.balance += abs(amount)
        self.transactions.append(abs(+amount))
        return abs(amount)
    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -=amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} You have:' \
                   '\n'.format(amount, self.balance)
    def get_first_name(self):
        return self.name
    def get_balance(self):
        return self.balance
    def recent_transactions(self):
        if len(self.transactions) < 1:
            return 0
        else:
            return self.transactions.pop()





print("///////////////////////////////////////")


from datetime import datetime
import datetime as dt

class Transaction(object):

    def __init__(self,name,children=[] ,timestamp=datetime.now()):
        self.name=name
        self.children = children
        self.timestamp = timestamp
        self.children = []
    def times(self,timestamp):
        self.timestamp=datetime.now()
        return timestamp
    def amount(self,childd):
        self.children.append(childd)
        return self.children

    def add_child(self, child,timestamp=datetime.now()):

        self.children.append((child,timestamp))
        return self.children

    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.children})'.format(self)

    def __str__(self):
        return 'timesatmp:{},amount:{}'.format(self.timestamp,self.children)


















