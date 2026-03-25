# Write code below 💖
class BankAccount:
  def __init__ (self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.balance = balance

  def deposit(self, num):
    self.balance = self.balance + num
    return self.balance
  
  def withdraw(self, num):
    self.balance= self.balance - num
    return num

  def display_balance(self):
    print(self.balance)

Monzo = BankAccount('Toluwani', 'Shodeinde', 3456, 'Savings', 4567, 100000.0)
Monzo.deposit(96)
Monzo.withdraw(25)
Monzo.display_balance()
