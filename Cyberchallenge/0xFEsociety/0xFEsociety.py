import string

sniff = []

with open ("./sniff.txt") as file:
    for line in file:
        sniff.append(line.replace("\n", ""))

words = []

with open ("./words.txt") as file:
    for line in file:
        words.append(line.replace("\n", ""))

C = [1] # C contains for every cell the numer of suggested words after i + 1 typed letters

t = 0
for line in sniff:
    if line != "-- end --":
        C[t] += 1

    else:
        C.append(0)
        t += 1

# now i should have saved all of the suggested words for every letter typed in

flag = ""

for c in range(len(C)):
    counter = 0

    for p in string.printable:

        for w in words:

            if w[:len(flag) - 1] == flag:
                counter += 1 
        
        if (counter == C[c]):
            flag.append(p)
        
        counter = 0

print (flag)
