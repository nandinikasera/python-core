class student:
    def __init__(self):
        self.name=""
        self.id=0
        self.chemistry_marks=0
        self.math_marks=0
        self.english_marks=0


    def setName(self,name):
        self.name=name

    def setID(self,id):
        self.id=id

    def setChemistry_marks(self,chemistry_marks):
        self.chemistry_marks=chemistry_marks

    def setMath_marks(self,math_marks):
        self.math_marks=math_marks

    def setEnglish_marks(self,english_marks):
        self.english_marks=english_marks

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getChemistry_marks(self):
        return self.chemistry_marks

    def getMath_marks(self):
        return self.math_marks

    def getEnglish_marks(self):
        return self.english_marks

p=student()

p.setName("nandini")
p.setID(21)
p.setChemistry_marks(98)
p.setMath_marks(88)
p.setEnglish_marks(77)

print(p.getName())
print(p.getID())
print(p.getChemistry_marks())
print(p.getMath_marks())
print(p.getEnglish_marks())