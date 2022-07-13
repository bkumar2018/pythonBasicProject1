#Dictionary: key-value pairs, unordered, mutable

mydict = {'name':"Barry", 'age': 24, 'city': 'pune'}
print(mydict)

value = mydict['name']
print(value)

mydict['phone'] = '555-5555'
print(mydict)

del mydict['phone']
print(mydict)

# popitem = mydict.pop('name')
# print(popitem)
# print(mydict)
# print(mydict.popitem())


if "name" in mydict:
    print(mydict['name'])
elif "city" in mydict:
    print(mydict['city'])
else:
    print("key not present")

try:
    print(mydict['city'])
except:
    print("Error")


for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

for k, v in mydict.items():
    print(k,v)

mydict_copy=mydict
print(mydict_copy)

mydict_copy['email'] = 'abc@yx.com'
print(mydict)
print(mydict_copy)

new_mydict = mydict.copy()
new_mydict['phone'] = '555-5555'
print(mydict)
print(new_mydict)


new_dict = dict(mydict)
new_dict['pin'] = 411031
print(mydict)
print(new_dict)
