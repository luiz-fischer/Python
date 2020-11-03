#JSON
import json

#Some JSON:
x = '{ "name":"John", "age":"38", "city":"Joinville" }'

#Parse x 
y = json.loads(x)

#Result 
print(y["age"])

#Convert from Python to JSON

#a Python Object (dict)
x = {
    "name":"John",
    "age":"38",
    "city":"Joinville"
}

#Convert into JSON
y = json.dumps(x)

#The result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))