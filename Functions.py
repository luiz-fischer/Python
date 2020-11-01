#Creating a Function
def myFunc():
    print("Hello with Function!!")

#Calling a Function
def myFunc():
    print("Hello with Function!!")

myFunc()

#Arguments
def myFunc(fname):
    print(fname + " Refsnes")

myFunc("Emil")
myFunc("Tobias")
myFunc("Linux")

#Number of Arguments
def myFunc(fname, lname):
    print(fname + " " + lname)

myFunc("Emil", "Refsnes")

#Arbitrary Arguments, *args
def myFunc(*kids):
    print("The youngest child is: " + kids[2])

myFunc("Emil", "Tobias", "Raul")

#Keyworld Arguments
def myFunc(child1, child2, child3):
    print("The youngest child is: " + child2)

myFunc(child1 = "Emil", child2 = "Tobias", child3 = "Raul")

#Arbitrary Keyworld Arguments, **kwargs
def myFunc(**kid):
    print("His last name is " + kid["lname"])

myFunc(fname = "Tobias", lname = "Tiboco")

#Default Parameter Value
def myFunc(country = "Joinville"):
    print("Im from " + country)

myFunc("Brazil")
myFunc("India")
myFunc()
myFunc("Canada")

#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "cherry"]

my_function(fruits)

#Return Values
def my_function(x):
    return 5 * x

print(my_function(3))

#The Pass Statement
def myFunc():
    pass

#Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\nRecursion Example Results")
tri_recursion(6)