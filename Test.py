import TresorHandler

#TH = TresorHandler.TresorHandler()

#TH.add("test_site", "Test_user", "test_pw", "xo79uedn")

with open('Salt.txt', "r+b") as salthandle:
    salt_1 = salthandle.read()

with open('Salt.txt', "r+b") as salthandle:
    salt_2 = salthandle.read()

if salt_1 == salt_2:
    print("Kein Fehler")



