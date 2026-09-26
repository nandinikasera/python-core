class A:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0

    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address

    def setAge(self,age):
        self.age = age

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getAge(self):
        return self.age


p = A()
p.setName("nandini")
p.setAddress("indore")
p.setAge(22)

print(p.getName())
print(p.getAddress())
print(p.getAge())
