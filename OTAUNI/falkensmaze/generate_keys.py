from Crypto.PublicKey import RSA
from Crypto.Protocol.KDF import PBKDF2

salt = 'SSBhbSBzZWVkIGRhdGEuIEtlZXAgbWUgZW5jb2RlZCB0byBnZW5lcmF0ZSB5b3VyIGtleQ=='
password = 'joshua'

master_key = PBKDF2(password, salt, count=10000)

def notRand(n):
    notRand.counter += 1
    return PBKDF2(master_key, str(notRand.counter), dkLen=n, count=1)

notRand.counter = 0

RSA_KEY = RSA.generate(4096, randfunc=notRand)
print RSA_KEY.exportKey('PEM')
