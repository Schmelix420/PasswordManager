# PasswordManager
A simple password manager.

This program creates and manage a password safe. The safe is a file with a list of dictionarys. Each dictionary consists of three entrys:
"What": The name of the site, program or whatever if the context of the username/password combination
"Username": The username
"Password": The password
The entrys are encrypted with cryptographys Fernet. See https://cryptography.io/en/latest/fernet/ for more details.
For each operation you need to enter the masterpassword.

When you first start the program it will create a "TresorFile" and an "SaltFile". The "TresorFile" is the password safe and the "SaltFile" is the salt. You need both files to get data from the password safe.

Methods:
add:
Adds a new entry to the safe file. Usage: ./PW_Manager add reddit JohNCena69 'qwertz'  Note: You have to add '' around the password so the linux command line includes specail caracters in the string

delete:
Deletes an entry from the safe file. Usage: ./PW_Manager delete reddit

get password:
Copies the password of the "What" to the clipboard. Usage: ./PW_Manager get password reddit

get username:
Copies the username of the "What" to the clipboard, Usage; ./PW_Manager get username reddit


Errors:
If you are 100% sure that the masterpassword you entered is correct check if the Salt file was changes recently. If yes you have a problem. Next time make a backup from it.
