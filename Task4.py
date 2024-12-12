class BankAccount():
    
    def __init__(self):
        self.ammount = 0
        self.record = [0]

    def deposit(self, value):
        self.ammount+= value
        return self.record.append(self.ammount)
        
    def withdraw(self, value):
        self.ammount-=value
        return self.record.append(self.ammount)
        
    def get_balance(self):
        for i in range(1, len(self.record)):
            type = 'deposit' if self.record[i] > self.record[i - 1] else 'withdrawl'
            print(f'Balance after {type}: {self.record[i]}')

account = BankAccount()
account.deposit(1000)
account.withdraw(200)
account.get_balance()