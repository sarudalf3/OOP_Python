class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 

    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

    def make_withdrawal (self, amount):
        if (self.account_balance - amount < 0):
            print("You don't have enough money to withdrawal")
        else:
            self.account_balance -= amount

    def display_user_balance (self):
        print(f"{self.name} has in the savings account {self.account_balance}.")

    def transfer_money (self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        self.display_user_balance()
        other_user.display_user_balance()

juanito = User(name='Juan Malaver', email='juanito@python.es')
eli = User(name='Eli Hernandez', email='tech@nasa.gov.org')
JuanPablo = User(name='Juan Pablo Castillo', email='customerservice@apple.com')

juanito.make_deposit(200)
juanito.make_deposit(100)
juanito.make_deposit(40)
juanito.make_withdrawal(80)
juanito.display_user_balance()

eli.make_deposit(600)
eli.make_deposit(245)
eli.make_withdrawal(400)
eli.make_withdrawal(500)
eli.display_user_balance()

JuanPablo.make_deposit(10000)
JuanPablo.make_withdrawal(1300)
JuanPablo.make_withdrawal(4500)
JuanPablo.make_withdrawal(4189)
JuanPablo.display_user_balance()

eli.transfer_money(JuanPablo,200)