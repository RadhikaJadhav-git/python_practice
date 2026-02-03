class Account:
    def __init__(self):
        self.__balance = 10000

    def get_balance(self):
        return self.__balance

acc = Account()
print("Balance:", acc.get_balance())
