filename = input("\033[46m [×] Enter Your Smtp List:  \033[0m ")
file = open(filename).read().split("\n\n")
for lines in file:
    try:
        line = lines.split("\n")
        host = line[0].split(": ")[1].strip()
        port = line[2].split(": ")[1].strip()
        user = line[3].split(": ")[1].strip()
        password = line[4].split(": ")[1].strip()
        if not user or not password: continue
        if not host or not port: continue
        with open("splited_smtps.txt",'a') as f: f.write(f"{host}|{port}|{user}|{password}\n")
    except:
        pass