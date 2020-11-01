#Class 
class myClass:
    x = 5
    print(x)

#Create Object
p1 = myClass()
print(p1.x)

#Create Class named Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
      print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
p1.myFunc()

#The Self Parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myFunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Mick", 56)
p1.myFunc()

#Modify Object Proprerties
p1.age = 40

del p1.age

del p1

class Person:
    pass