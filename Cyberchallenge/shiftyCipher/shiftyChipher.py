from pwn import remote
IP = "3.69.144.169"
PORT = "8003"

conn = remote(IP, PORT)

for i in range (4):
    print(conn.recvline().decode())

s = conn.recvline().decode().replace("\n", "")
print(s)
t = ""

#conn.recvline()
shift = 13

for i in s:
    if i != ' ':
        t += chr((ord(i) + shift - 97) % 26 + 97)
    else:
        t += ' '

print(t, '\n')
conn.sendline(t.encode())

################################

shift = conn.recvline().decode()
print(shift)

shift = shift.replace('\n', '').split(' ')
shift = shift[-3]

print(shift, '\n')

s = conn.recvline().decode().replace('\n', '')
print(s)

ans = ''

for i in s:
    if i != ' ':
        ans += chr((ord(i) - int(shift) - 97) % 26 + 97)

    else:
        ans += ' '

print(ans)

conn.sendline(ans.encode())
print(conn.recvline().decode())
print(conn.recvline().decode())

s = conn.recvline().decode().replace('\n', '')
print(s)

for i in range(0, 25):
    ans = ''
    shift = i

    for c in s:
        ans += chr((ord(c) - shift - 97) % 26 + 97)

    print(ans, '\n')