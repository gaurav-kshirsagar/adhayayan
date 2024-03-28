#Design a class BankAccount with private attributes __balance and a private method
#__validate_transaction that checks if a transaction is valid. Use encapsulation to protect the
#balance.

class BankAccount:
    __balance = 0

    def deposite(self,amt):
        self.__balance += amt
        print(amt,"Rs Deposited")

    def withdraw(self,amt):
        self.__balance -= amt
        print(amt,"Rs Withdraw")

    def getbalance(self):
        return self.__balance

    def ____validate_transaction(self):
        pass

bnkobj = BankAccount()

bnkobj.deposite(100)
bnkobj.getbalance()
bnkobj.withdraw(50)
bnkobj.getbalance()


    
