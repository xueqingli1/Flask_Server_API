import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
print(y)
# the result is a Python dictionary:
print(y["age"])


info = {
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

# convert into JSON:
json_format = json.dumps(info)

parsed = json.loads(json_format)

# the result is a JSON string:

print(parsed["cars"][0]["model"])


complicated = { 
  "accounting" : [   
                     { "firstName" : "John",  
                       "lastName"  : "Doe",
                       "age"       : 23 },

                     { "firstName" : "Mary",  
                       "lastName"  : "Smith",
                        "age"      : 32 }
                 ],                            
  "sales"      : [ 
                     { "firstName" : "Sally", 
                       "lastName"  : "Green",
                        "age"      : 27 },

                     { "firstName" : "Jim",   
                       "lastName"  : "Galley",
                       "age"       : 41 }
                 ] 
} 

# convert into JSON:
json_format = json.dumps(complicated)
print("this is json_format", json_format)
parsed = json.loads(json_format)

# the result is a JSON string:
# print(parsed["accounting"][0]["age"])