dictionary = {}

with open ("dati.txt", "rt") as input:
    line = " "

    while line is not None and line not in ["", "\n"]:
        line = input.readline()
        #line.replace("\n", "4") #non funziona, tiene il \n

        elementi = line.split(" ")
        elementi[1].replace("\n", "")

        if (elementi[1] not in dictionary.keys()):
            dictionary[elementi[1]].append(elementi[0]) #append() aiuta con delle exceptions a capire cosa hai sbagliato negl inserimenti
        else:
            dictionary[elementi[1]].append(elementi[0])

for key in dictionary.keys():
    print(f"eta: {key}, nomi: {dictionary[key]}")
