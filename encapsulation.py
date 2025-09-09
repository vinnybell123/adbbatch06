class bank_account():
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    

    def deposite(self,amount):
        self.__balance += amount
        print(f"deposited amount {amount} and the balance is {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw amount is {amount} and the balance is {self.__balance}")
        else:
            print("insufficient fund")
    def __get_balance(self):
        return self.__balance
    def show_balance(self):
        return self.__balance()

account = bank_account("1234", 10000)
print("initial balance")
#account.deposite(3000)
account.withdraw(9000)


