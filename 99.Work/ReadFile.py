
rFile = open("hza_gather_3.sql", "r", encoding = "utf-8")

wFile = open("saury.sql", "a")

line = rFile.readline()

toWrite = False

count = 0

while line:
    if line.find("hza_user_place") >= 0:
        toWrite = True
    if toWrite:
        if line.find(",374657") >= 0:
            print(line)
            wFile.write(line)
    line = rFile.readline()
#    if toWrite == False:
#        if line.find("hza_user_place") >= 0:
#            toWrite = True
#    if toWrite:
#        print(line)
#        count = count + 1
#        wFile.write(line)
#    line = rFile.readline()
#    if count > 1000:
#        break
#        if toWrite:
#            if line.find("TABLE") >= 0:
#                break
