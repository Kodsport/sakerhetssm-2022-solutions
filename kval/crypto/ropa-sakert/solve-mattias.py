#!/usr/bin/env python3
from pwn import *

p = 84110607885424435789520899428064591379192332213262905744967612163375651444019
q = 67829743147343394076748419759397419634107631589392973908325370212997597011613
d = 2213586969474081412462124297644928143705359494098619937248568620130781387315122350943336924430305120870587389920200952126423912501926700805309031037044579
N = p*q

m = int(b"Hi Alice! This is a secret message.".hex(), 16)
e = pow(d, -1, (p-1)*(q-1))
c = pow(m, e, N)

r = remote("localhost", 50000)
r.sendline(str(c))
r.interactive()