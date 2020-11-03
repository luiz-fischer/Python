#Import a Module
import mymodule

#Use a Module
mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a) 

#Re-naming a Module
import mymodule as mx

a = mx.person1["age"]
print(a) 

#Built-in Modules
import platform

x = platform.system()
print(x) 

#Using the dir() Function
x = dir(platform)
print(x) 

from mymodule import person1

print (person1["age"])