import zipfile, sys
file = open(sys.argv[1], "r")
dico = open(sys.argv[2], "r")
passwords = dico.readlines()
for pwd in passwords:
    try:
        for info in file.infolist():
            fname = info.filename
            print("Attempt to crack", str(pwd))
            data = file.read(fname, str(pwd))
            print("Pwd found :", str(pwd))
            break
    except Exception as e:
        print(e)