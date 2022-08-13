# json-javasrcipt object notation
import json
a={"name":"anees","age":23,"language":"python,js","boolean":False}
print(a)
print(type(a))
# converting the json file
b=json.dumps(a)
print(b)
print(type(b))

# converting dictionary string format to normal dictionary object
data='{"var1":"anees","var2":56}'
print(data)
print(type(data))
parsed=json.loads(data)
print(parsed)
print(type(parsed))