import json
import yaml
#Example of json
x = '{"name" : "John", "age" : "30", "city" : "New York"}'
# parse json
y = json.loads(x)
print("The output json file is ", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["city"])