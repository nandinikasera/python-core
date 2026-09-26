class person:
    AGE = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age




    def get_age(self):
        if self.age > person.AGE:
            print("can vote")
        else:
            print("can not vote ")


p = person("nandini", 22)
print(person.AGE)
print(p.age)
print(p.name)
p.get_age()
