from sympy import factorint
from pwn import remote

IP = "3.69.144.169"
PORT = "8012"
conn = remote(IP, PORT)

n = int(conn.recvline().decode()[3:])
e = int(conn.recvline().decode()[3:])
c = conn.recvline().decode()[5:]
c = c[:-4]

C = c.split(", ")

#skippo 2 lines
conn.recvline()
conn.recvline()

#troviamo p e q fattorizzando n sapendo che sono entrambi numeri primi
facts = factorint(n)
p, q = facts.keys()

dec = []
phi = (q - 1)*(p - 1)

for i in c:
    i = int(i)

    #d = 
    """
    cerco l'inverso moltiplicativo modulo phi(n) = 1 di e, quindi e * d % phi = 1, sono interessato a d:
    eq diofantea: ax + by = c; x e y ottenibile conoscendo a, b, c; utile?

    si pk:
    ed * kphi = 1 // conosco e, conosco phi e conosco 1, d e k sno x e y
    """
    dec.append(pow(i, d, n)) #seguendo il teorema m**ed % phi(n) = m

print(dec)