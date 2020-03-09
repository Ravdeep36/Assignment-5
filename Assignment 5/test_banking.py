from banking import BankAccount
from banking import Transaction

a = BankAccount('Purcell')
print('deposit =', a.deposit(100))
print('recent transaction is:', a.recent_transactions())
print('account balance =', a.get_balance())
print('withdrawal =', a.withdrawal(90))
print('recent transaction is:', a.recent_transactions())
print('account balance =', a.get_balance())
print('deposit =', a.deposit(10))
print('account balance =', a.get_balance())



print('FOR TRANSACTION')
import datetime as dt


person1 = Transaction('li')
print('lk',str(person1))
person1=person1.add_child(100)
print('lk',str(person1))



