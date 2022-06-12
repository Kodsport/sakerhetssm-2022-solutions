import pwn

ADDR, PORT = 'localhost', 50000

p = pwn.remote(ADDR, PORT, ssl=True)
p.recv()
p.send(b'1\n')
print(p.recvline())
p.send(b'2\n')
