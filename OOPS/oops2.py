                                                                                    #BANK ACCOUNT
class bank:
    def AccCreate(self,accno,acctype,name):
        self.accno=accno
        self.acctype=acctype
        self.name=name
        self.balance=3000
    def deposit(self,amount):
        self.balance+=amount
        print("your account has been credited",amount,"/-")
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient fund")
        else:
            self.balance=amount
            print("Your account has been debited with amount R.s",amount,"/-")
    def balanceEnq(self):
            print("your current balance is",self.balance)
b=bank()
b.AccCreate(123,"sav","Surya")
b.deposit(10000)
b.balanceEnq()

