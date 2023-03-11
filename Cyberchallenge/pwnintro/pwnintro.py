from pwn import remote
IP = '3.69.144.169'
PORT = '8001'

conn = remote(IP, PORT)

conn.recvline()
n = int(conn.recvline().decode().split(' ')[1])
conn.recvline()

print(n)

for i in range (0, n):
    list = (conn.recvline().decode()).split(' ')
    print(list[:3])

    if list[1] == '+':
        t = int(list[0]) + int(list[2])
        t = str(t)
        conn.sendline(t.encode())

    elif list[1] == '-':
        t = int(list[0]) - int(list[2])
        t = str(t)
        conn.sendline(t.encode())

    elif list[1] == '*':
        t = int(list[0]) * int(list[2])
        t = str(t)
        conn.sendline(t.encode())

    elif list[1] == '//':
        t = int(list[0]) // int(list[2])
        t = str(t)
        conn.sendline(t.encode())

    print(conn.recvline().decode(), i)

print(conn.recvline().decode())