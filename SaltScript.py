import os

with open("Salt.txt", "w") as file:
    file.write(str(os.urandom(16)))