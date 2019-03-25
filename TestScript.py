import json


Passwords = [ {"What": "tabletoptactics", "Username": "Test1234", "Password": "qwerasd" },
              {"What": "Bahn", "Username": "Correro1337", "Password": "yxcvb"},
              {"What": "pornhub", "Username": "Schmelix420", "Password": "polki"}
            ]

#with open('Jsonfile.json', 'w') as data_file:
#    data_file.write(json.dumps(Passwords))



with open('Jsonfile.json', encoding='utf-8') as data_file:
   data = json.loads(data_file.read())

print(data)
print(Passwords)

for i in data:
    if "Bahn" in i.values():
        print("Juhu")
    else:
        print("Moep")





