from pwn import remote

def MCD(a, b): #tutto ciò per il teorema di euclide esteso
    if a < b: #voglio che a sia strettamente maggiore di b
        a, b = b, a
    
    while a % b != 0: # finché b non è divisiore di a
        a, b = b, a % b # a è b, e b corrisponde al resto della divisione intera di a per b

    return b # ritorna il resto dell'ultima divisione intera di a per b

def diophantine(a, b, c):
    #cerca in che rapporti sono i a,c e b,c 
    d = MCD(a, b)
    if c % d != 0: # c % d == 0 vuol dire che d è divisore di c o che d == 1
        return('impossible')
    
    else: 
        if d == c:
            return('1 0')

        else:
            y, x = MCD(a, c), MCD(b, c)
            
            if a*x + b*y == c:
                return(f'{x} {y}')
            else:
                return('impossible')

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
    a, b, c = list.split(' ')

    ans = diophantine(int(a), int(b), int(c))
    conn.sendline(ans.encode())
    conn.recvline().decode()

for i in range (0, 4):
    conn.recvline().decode()

