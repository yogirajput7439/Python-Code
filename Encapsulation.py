# ENCAPSULATION 

class bank:

  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amount):
    self.balance += balance

  def show_balance(self):
    print(self.balance)

b1 = bank(1000)

b1.deposit(500)
b1.show_balance()
