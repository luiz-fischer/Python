import datetime


x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x)

#String Method
print(x.strftime("%B")) 

#Math
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#ABS
x = abs(-8.55)
print(x)

#Power
x = pow(2, 6)
print(x)

import math

x = math.sqrt(64)
print(x)
