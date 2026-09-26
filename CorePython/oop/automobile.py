class car:
    GEAR=6
    def __init__(self):
        self.color = ""
        self.type = ""
        self.speed =0




    def setcolor(self,color):
        self.color = color

    def setType(self,type):
        self.type = type

    def setspeed(self,speed):
        self.speed = speed


    def getcolor(self):
        return self.color

    def getType(self):
        return self.type

    def getspeed(self):
        return self.speed




    def get_accelarator(self):
        if self.speed>=400:
            print("plz apply breaks")

        else:
            self.speed = self.speed + 10
            print("tatal speed after accelaration is", self.speed)


    def get_break(self):
        if self.speed==0:
            print("car is not moving")

        else:
            self.speed = self.speed - 10
            print("total speed after applying breaks is", self.speed)


    def get_gear(self,no):
        if no>car.GEAR:
            print("there is no such gear exists")
        elif no==1:
            self.speed=20
            print("speed after applying gear1",self.speed)
        elif no==2:
            self.speed=40
            print("speed after applying gear2",self.speed)

        elif no==3:
            self.speed=60
            print("speed after applying gear3",self.speed)

        elif no==4:
            self.speed=80
            print("speed after applying gear4",self.speed)

        elif no==5:
            self.speed=100
            print("speed after applying gear5",self.speed)

        elif no==6:
            self.speed=120
            print("speed after applying gear6",self.speed)

        elif no==0:

            print("car will move in reverse")



p = car()
p.setcolor("red")
p.setType("bmw")
p.setspeed(70)



print(p.getcolor())
print(p.getType())
print(p.getspeed())
print(car.GEAR)


p.get_accelarator()
p.get_break()
p.get_gear(7)
p.get_gear(3)








