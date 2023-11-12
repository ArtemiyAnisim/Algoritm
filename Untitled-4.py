class BankAccount:
     def __init__(self, balance, interest_rate, name, surname):         self.name = name
         self.surname = surname#         self.balance = balance
         self.interest_rate = interest_rate
         self.transactions = []

     def klient(self):
         print(f'Имя и фимилия: {self.name} {self.surname}')

     def deposit(self, amount):
         self.balance += amount
         self.transactions.append(f"Внесение наличных на счет: {amount}")

     def withdraw(self, amount):
         if self.balance >= amount:
            self.balance -= amount
           self.transactions.append(f'Снятие наличных: {amount}')
        else:
             print("Недостаточно средств на счете")

     def add_interest(self):
         sum_balance_interest = self.balance * self.interest_rate
         self.balance += sum_balance_interest
         self.transactions.append(f'Начислены проценты по вкладу {sum_balance_interest}')

     def history(self):
         for transaction in self.transactions:
             print(transaction)


 account = BankAccount(100, 1, 'Лёша', 'Александров')
 account.klient()
 account.deposit(13000)
 account.withdraw(5000)
 account.add_interest()
 account.history()
