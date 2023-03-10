from pwn import remote

def MCD(a, b): #tutto ciò per il teorema di euclide esteso
    if a < b: #voglio che a sia strettamente maggiore di b
        a, b = b, a
    
    while a % b != 0: # finché b non è divisiore di a
        a, b = b, a % b # a è b, e b corrisponde al resto della divisione intera di a per b

    return b # ritorna il resto dell'ultima divisione intera di a per b

def diophantine(a, b, c):
    #cerca in che rapporti sono i a,c e b,c 
    if MCD(a, c) == MCD(b, c) == c:
        return ('1 0')
    
    elif MCD(a, c) == c and MCD(b, c) != c:
        return('0 1')
    
    elif MCD(b, c) == c and MCD(a, c) != c:
        return('1 0')

    else:
        x, y = MCD(b, c), MCD(a, c)
        if a * x + b * y != c:
            return('impossible')
        else:
            return (f'{x} {y}')

IP = "3.69.144.169"
PORT = "8013"

conn = remote(IP, PORT)

for line in range (0, 5):
    conn.recvline()

challenge = "2"
conn.sendline(challenge.encode())

n = conn.recvline().decode() #qui dovrebbe mandare solve n challenges
n = n[6]

for i in range(0, int(n)):
    list = []
    list = conn.recvline().decode()
    print (list)

    conn.sendline(str(diophantine(int((list.split(' '))[0]), int((list.split(' '))[1]),int((list.split(' '))[2]))).encode())
    conn.recvline().decode()

conn.recvline().decode()
conn.recvline().decode()
conn.recvline().decode()
conn.recvline().decode()

