#Filehandling
import os
import json

#cryptography
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class TresorHandler:
    def __init__(self):
        #Get the contant of the tresor file
        if os.path.isfile("TresorFile.json"):
            with open('TresorFile.json', 'r', encoding='utf-8') as data_file:
                self.TresorData = json.loads(data_file.read())
        else:
            self.TresorData = list()

        #Get the Salt value. If there is no salt file, create a salt value and create the salt file
        if os.path.isfile("Salt.txt"):
            with open('Salt.txt', "r+b") as salthandle:
                self.salt = salthandle.read()
        else:
            self.salt = os.urandom(16)
            with open('Salt.txt', "w+b") as salthandle:
                salthandle.write(self.salt)


    def add(self, site_to_add, user_to_add, password_to_add, masterpassword):
        password = masterpassword.encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

        f = Fernet(key)
        encrypted_site = f.encrypt(site_to_add.encode())
        encrypted_user = f.encrypt(user_to_add.encode())
        encrypted_pw = f.encrypt(password_to_add.encode())

        for i in self.TresorData:
            if str(encrypted_site) in i.values():
                print("The site " + site_to_add + " already exists. If you want to change it,"
                                                      " you have to delete it first.")
                return


        self.TresorData.append({"What": str(encrypted_site), "Username": str(encrypted_user),
                                         "Password": str(encrypted_pw)})

        with open('TresorFile.json', 'w', encoding='utf-8') as data_file:
            data_file.write(json.dumps(self.TresorData))




