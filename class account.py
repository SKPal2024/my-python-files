class Account:
    def __init__(self,acc_no,balance):
        self.acc=acc_no
        self.bal=balance

    def credit(self,amount):
        a=self.bal+amount
        print("Rs",amount,"is credited to your account")
        print("final balance is ",a)

    def debit(self,amount):
        b=self.bal-amount
        print("Rs",amount,"is debited from your account")
        print("final balance is ",b)
acc1=Account(100,70000000)
acc1.debit(30000)
acc1.credit(50000)