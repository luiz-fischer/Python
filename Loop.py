#WHILE
i = 1
while i < 6:
  print(i)
  i += 1

#The Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#The Continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The Else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#FOR
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
    print(x)

#The Break Statement
fruits = ["Apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#Exit the loop when x is "banana", but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The Continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#The Range Function
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

#Else in For Loop
for x in range(6):
    print(x)
else: 
    print("Finally Finished")

#Nested Loops
adj = ["Red", "Big", "Tasty"]
fruits = ["Apple", "Banana", "Cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#The Pass Statement
for x in [0, 1, 2]:
    pass