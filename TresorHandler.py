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
                self.__TresorData = json.loads(data_file.read())
        else:
            self.__TresorData = list()

        #Get the Salt value. If there is no salt file, create a salt value and the salt file
        if os.path.isfile("Salt.txt"):
            with open('Salt.txt', "r+b") as salthandle:
                self.__salt = salthandle.read()
        else:
            self.__salt = os.urandom(16)
            with open('Salt.txt', "w+b") as salthandle:
                salthandle.write(self.__salt)

    def __createFernet(self, masterpassword):
        password = masterpassword.encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.__salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

        return Fernet(key)

    def add(self, site_to_add, user_to_add, password_to_add, masterpassword):
        f = self.__createFernet(masterpassword)

        for dic in self.__TresorData:
            try:
                decrypted_site = f.decrypt(dic["What"].encode())
            except:
                print("Wrong masterpassword.")
                return

            if site_to_add == decrypted_site.decode():
                print("The site " + site_to_add + " already exists. If you want to change it,"
                                                  " you have to delete it first.")
                return

        encrypted_site = f.encrypt(site_to_add.encode())
        encrypted_user = f.encrypt(user_to_add.encode())
        encrypted_pw = f.encrypt(password_to_add.encode())

        self.__TresorData.append({"What": encrypted_site.decode(), "Username": encrypted_user.decode(),
                                         "Password": encrypted_pw.decode()})

        with open('TresorFile.json', 'w', encoding='utf-8') as data_file:
            data_file.write(json.dumps(self.__TresorData))


    def delete(self, site_to_delete, masterpassword):
        f = self.__createFernet(masterpassword)

        for i in range(len(self.__TresorData)):
            try:
                decrypted_site = f.decrypt(self.__TresorData[i]["What"].encode())
            except:
                print("Wrong masterpassword.")
                return

            if site_to_delete == decrypted_site.decode():
                del(self.__TresorData[i])

                with open('TresorFile.json', 'w', encoding='utf-8') as data_file:
                    data_file.write(json.dumps(self.__TresorData))

                print("Deleted: " + site_to_delete)
                return

        print("Site " + site_to_delete + " is not on the list.")

    def get_password(self, site_to_get_from, masterpassword):
        f = self.__createFernet(masterpassword)

        for dic in self.__TresorData:
            try:
                decrypted_site = f.decrypt(dic["What"].encode())
            except:
                print("Wrong masterpassword.")
                return

            if site_to_get_from == decrypted_site.decode():
                password = f.decrypt(dic["Password"].encode())
                return password.decode()

        print("Site " + site_to_get_from + " is not on the list.")

    def get_user(self, site_to_get_from, masterpassword):
        f = self.__createFernet(masterpassword)

        for dic in self.__TresorData:
            try:
                decrypted_site = f.decrypt(dic["What"].encode())
            except:
                print("Wrong masterpassword.")
                return

            if site_to_get_from == decrypted_site.decode():
                password = f.decrypt(dic["Username"].encode())
                return password.decode()

        print("Site " + site_to_get_from + " is not on the list.")



