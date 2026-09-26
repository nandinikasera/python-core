class account:
    def __init__(self):
        self.name=""
        self.accountNo=0
        self.accountBalance=0



    def setName(self,name):
        self.name=name

    def setAccountNo(self,accountNo):
        self.accountNo=accountNo

    def setAccountBalance(self,accountBalance):
        self.accountBalance=accountBalance

    def getName(self):
        return self.name

    def getAccountNo(self):
        return self.accountNo

    def getAccountBalance(self):
        return self.accountBalance



p=account()

p.setName("nandini")
p.setAccountNo(21)
p.setAccountBalance(98)


print(p.getName())
print(p.getAccountNo())
print(p.getAccountBalance())
