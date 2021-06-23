class BankAccount:
	def __init__(self, int_rate=0.001, balance=0):
		self.intRate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self
	
	def withdraw(self, amount):
		if self.balance > amount:
			self.balance -= amount
		else: 
			print("Your balance isn't enough to withdraw the amount")	
		return self

	def display_account_info(self):
		print(f"balance: {self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance*(1+self.intRate)
		return self	

checking = BankAccount(0.5, 20)
saving = BankAccount(balance=100)

checking.deposit(300).deposit(450).deposit(350).withdraw(1000).yield_interest().display_account_info()
saving.deposit(800).deposit(450).withdraw(100).withdraw(550).withdraw(500).withdraw(300).yield_interest().display_account_info()