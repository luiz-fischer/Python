#Arrays

cars = ["BMW", "Ferrari", "Volvo"]

#Access de elements of an Array

x = cars[1]
print(x)

cars[1] = "Toyota"

#The length of an Array
x = len(cars)
print(x)

#Looping Arrays Elements
for x in cars:
    print(x)

#Adding Array Elements
cars.append("Honda")

#Removing Array Element
cars.pop(1)

cars.remove("Honda")