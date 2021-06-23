class BankAccount:
    def __init__(self, int_rate=0.001, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
	
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else: 
            print("insufficient Funds in your account")        
        return self

    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
        return self	

    def __str__(self):
        """Account Information"""
        return f"Int rate: {self.int_rate} \nBalance: {self.balance}" 


class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email, num_account):
        self.name = name    
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0) 
        self.accounts = {num_account: self.account}

    def open_account(self, num_account, int_rate, balance):
        self.accounts[num_account] = BankAccount(int_rate, balance)
        return self
    
    def make_deposit(self, num_account, amount):
        self.accounts[num_account].deposit(amount)	
        return self

    def make_withdraw(self, num_account, amount):
        self.accounts[num_account].withdraw(amount)
        return self

    def transfer_money(self,num_account,other_user, other_num_account, amount):
        if (self.accounts[num_account].balance > amount):
            self.accounts[num_account].withdraw(amount)
            other_user.accounts[other_num_account].deposit(amount)
            print(f"Account {num_account} of {self.name} has {self.accounts[num_account].balance} ")
            print(f"Account {other_num_account} of {other_user.name} has {other_user.accounts[other_num_account].balance} ")  
            print("")
        else:
            print("insufficient Funds in your account")
        return self

    def show_balance(self):
        for account, balance in self.accounts.items():
            print(f"{self.name}\naccount number: {account}\ninterest rate: {balance.int_rate}\nBalance: {balance.balance}\n------\n")
        return self

if __name__ == "__main__":
    #Ruben's first account 
    rube = User("ruben Miranda","ruben.miranda@amazon.com",1564)
    rube.open_account(1646,0.02,20)
    rube.open_account(1954,0.01,50)

    rube.show_balance()

    #Norah account 
    norah = User("Norah Jones","norah.jones@jazzmusic.com",5632)
    norah.show_balance()

    rube.make_deposit(1646,200)
    rube.make_deposit(1564,800)
    norah.make_deposit(5632,8000)

    rube.show_balance()
    norah.show_balance()

    rube.make_withdraw(1564,400)
    rube.make_withdraw(1954,100)
    norah.make_withdraw(5632,7900)

    rube.show_balance()
    norah.show_balance()    

    rube.transfer_money(1646, norah , 5632, 200) 
    rube.show_balance()
    norah.show_balance()
    