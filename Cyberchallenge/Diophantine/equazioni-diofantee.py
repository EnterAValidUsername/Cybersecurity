from pwn import remote

IP = "3.69.144.169"
PORT = "8013"

conn = remote(IP, PORT)

for line in range (0, 5):
    conn.recvline()

challenge = "2"
conn.sendline(challenge.encode())

n = conn.recvline().decode().split(' ') #qui dovrebbe mandare solve n challenges
n = n[1]


def diophantine(a, b, c):
    assert (
        c % greatest_common_divisor(a, b) == 0
    )  # greatest_common_divisor(a,b) function implemented below
    (d, x, y) = extended_gcd(a, b)  # extended_gcd(a,b) function implemented below
    r = c / d
    return (r * x, r * y)

def greatest_common_divisor(a, b):
    if a < b:
        a, b = b, a
 
    while a % b != 0:
        a, b = b, a % b
 
    return b
 
 
# Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcd(a,b)
 
 
def extended_gcd(a, b):
    assert a >= 0 and b >= 0
 
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
 
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
 
    return (d, x, y)

##############

for i in range(int(n)):
    # risolvo le equzioni diofantee
    list = conn.recvline().decode().replace('\n', '').split(' ')
    print(i, int(list[0]), int(list[1]), int(list[2]))
    conn.sendline(str(diophantine(int(list[0]), int(list[1]), int(list[2]))).encode())
    #print(conn.recvline().decode()) # se tutto va bene ad ogni giro printa 'Correct!'

print(conn.recvline().decode()) # flag??