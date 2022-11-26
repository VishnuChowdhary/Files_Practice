class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return "Current Balance: ", self.balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
            return "Current Balance: ", self.balance
        else:
            print("Insufficient Balance!")


acct1 = BankAccount('Vishnu', 1000)
print("Account Holder: " + acct1.owner)
print("Available Balance: ", acct1.balance)
deposit = int(input("Enter the amount to deposit: "))
print(acct1.deposit(deposit))
withdraw = int(input("Enter the withdraw amount: "))
print(acct1.withdraw(withdraw))
