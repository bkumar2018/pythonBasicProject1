
import json

json_string= '''{
"people":[
                {
                        "name": "Birender",
                        "phone":"8600141490",
                        "languages": ["English", "Hindi"]
                },
                {
                        "name": "Abhivardhan",
                        "phone":null,
                        "languages": ["English", "Fench"]
                }
        ]
}
'''

#print(json_string)

data = json.loads(json_string)
print(data)
print(type(data))
print(type(data["people"]))

print(data["people"])

for person in data["people"]:
    print(person['name'], person['phone'], person['languages'])

for person in data["people"]:
    del person['phone']

print(data["people"])

with open("jsonData.json",'w') as f:
    json.dump(data,f,indent=2)





