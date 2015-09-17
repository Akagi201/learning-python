
import json

a = json.dumps({'a':1, 'b':2})
print(type(a))
b = json.load("{'a':1, 'b':2}")
print(type(b))