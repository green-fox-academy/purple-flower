class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, balance):
        self.balance -= balance

    def receive(self, balance):
        self.balance += balance

    def print_balance(self):
        print("Balance of")
        print(self.name)
        print("is:")
        print(self.balance)

    def transfer(self, other, balance):
        self.pay(balance)
        other.receive(balance)

lilla = BankAccount("Lilla Virag", 10000)
lilla.receive(10500)

feri = BankAccount("Feri", 7000000)

lilla.transfer(feri, 1000)

lilla.print_balance()
feri.print_balance()
