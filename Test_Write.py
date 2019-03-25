import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

import json

Passwords = [ {"What": "tabletoptactics", "Username": "Test1234", "Password": "qwerasd" },
              {"What": "Bahn", "Username": "Correro1337", "Password": "yxcvb"},
              {"What": "pornhub", "Username": "Schmelix420", "Password": "polki"}
            ]

#Eingaben die vom Benutzer kommen
password = "qwer"

data = []

if os.path.isfile("Jsonfile.json"):
    with open('Jsonfile.json', 'r', encoding='utf-8' ) as data_file:
        data = json.loads(data_file.read())

data.append( {"What": "Second Entry", "Username": "TTTT", "Password": "jfhghjtj" } )

with open('Jsonfile.json', 'w', encoding='utf-8' ) as data_file:
    data_file.write(json.dumps(data))