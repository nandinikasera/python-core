class Account:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.balance = 0
        self.countw=0
        self.cd = 0


    def setName(self,name):
        self.name = name

    def setType(self,type):
        self.type = type

    def setBalance(self,balance):
        self.balance = balance

    def setcountw(self,countw):
        self.countw = countw
    def setcd(self,cd):
        self.cd = cd

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getBalance(self):
        return self.balance

    def getcountw(self):
        return self.countw

    def getcd(self):
        return self.cd

    def get_deposite(self,amt):
        if self.cd>=5:
            print("can not deposite more then 5 times")
        elif amt>=100000:
            print("cannot deposite more then1 lackh at once ")
        else:
            self.balance = self.balance + amt
            print("tatal balance is", self.balance)
            self.cd+=1

    def get_withdrow(self,amt):
        if self.countw<5:
            if amt > self.balance:
                print("insufficient ammout")
            elif amt>=50000:
                print("cannot withdrow more then 50000")
            else:
                self.balance = self.balance - amt
                print("total balance is", self.balance)
                self.countw+=1

        else:
            print("cannot do more then 5 withdrower")



p = Account()
p.setName("nandini")
p.setType("saving")
p.setBalance(100000)
p.setcountw(0)

print(p.getName())
print(p.getType())
print(p.getBalance())
print(p.getcountw())

p.get_deposite(50)
p.get_withdrow(30)
p.get_withdrow(40)
p.get_withdrow(50000)
p.get_withdrow(60)
p.get_deposite(50)
p.get_deposite(50)
p.get_deposite(50)
p.get_deposite(100000)


