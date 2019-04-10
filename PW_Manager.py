#!/usr/bin/python3
import sys
import getpass
import pyperclip
import TresorHandler
from codecs import decode


if len(sys.argv) < 2:
    print("To few arguments. \n"
          "Example: ./PW_Manager.py get password reddit. - Copies the password for reddit in the clipboard.")
    sys.exit()

TH = TresorHandler.TresorHandler()

if sys.argv[1] == "add":
    if len(sys.argv) < 5:
        print("To few arguments. \n"
              "Example: ./PW_Manager.py add reddit User1337 qwertz - Adds the entry for reddit.")
    else:
        masterpassword = getpass.getpass("enter Key :")
        TH.add(sys.argv[2], sys.argv[3], sys.argv[4], masterpassword)
elif sys.argv[1] == "delete":
    if len(sys.argv) < 3:
        print("To few arguments. \n"
              "Example: ./PW_Manager.py delete reddit - Deletes reddit from the list.")
    else:
        masterpassword = getpass.getpass("enter Key :")
        TH.delete(sys.argv[2], masterpassword)
elif sys.argv[1] == "get":
    if len(sys.argv) < 4:
        print("To few arguments. \n"
              "Example: ./PW_Manager.py get password/username reddit - Copies the password or the user "
              "to the clipboard.")
    else:
        masterpassword = getpass.getpass("enter Key :")
        if sys.argv[2] == "password":
            pyperclip.copy(TH.get_password(sys.argv[3], masterpassword))
            print("Password copied to the clipboard.")
        elif sys.argv[2] == "username":
            pyperclip.copy(TH.get_user(sys.argv[3], masterpassword))
            print("Username copied to the clipboard.")
        else:
            print("Error: Third argument has to be password or username. \n"
                  "Example: ./PW_Manager.py get password/username reddit - Copies the password or the user for reddit "
                  "to the clipboard.")
else:
    print("Error: Second argument has to be add, delete or get. \n"
          "Eample: ./PW_Manager.py get password reddit. - Copies the password for reddit in the clipboard.")
