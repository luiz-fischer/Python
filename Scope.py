#Scope
def myFunc():
    x = 300
    print(x)

myFunc()

#Function inside Function
def muFunc():
    x = 350
    def myInnerFunc():
        print(x)
    myInnerFunc()

myFunc()

x = 320

def myFunc():
    global x    
    x = 200

myFunc()

print(x)
