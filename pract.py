class BankAccount:
    accountNumber: int = 0
    balance: float = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance;
    
acc1 = BankAccount()
acc_num = int(input("Enter your account number: "))
acc1.accountNumber = acc_num

# choice = int(input("Enter 1 for withdawal o 2 for deposit:"))

amount = float(input("Enter amount to deposit:"))
acc1.deposit(amount)
print(f"current balance: {acc1.getBalance()}")

amount = float(input("Enter amount to withdraw:"))
acc1.withdraw(amount)
print(f"current balance: {acc1.getBalance()}")

# if choice == 1:
#     amount = float(input("Enter amount for withdrawal:"))
#     if acc1.balance <= amount:
#         print("Insufficient balance.")
#     else:
#         acc1.withdraw(amount)

# elif choice == 2:
#     amount = float(input("Enter amount to deposit:"))
#     acc1.deposit(amount)

# print(f"current balance: {acc1.getBalance()}")
