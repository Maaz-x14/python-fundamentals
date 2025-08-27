class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"{self.name} is talking")


person1 = Person("Maaz", 20)
print("Name:", person1.name)
print("Age:", person1.age)
person1.talk()

person2 = Person("Aena", 23)
print("Name:", person2.name)
print("Age:", person2.age)
person2.talk()
