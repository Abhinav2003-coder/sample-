class account:

    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,ammount):
        self.balance -= ammount
        print("Rs.",ammount,"was debited")
        print("total balance =",self.get_balance())

    def cradit(self,ammount):
        self.balance += ammount
        print("Rs.",ammount,"was cradited")
        print("total balance =",self.get_balance())
    
    def get_balance(self):
        return self.balance
        

acc1 = "account"(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(1000)
