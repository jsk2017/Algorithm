import binascii
import sys
from Crypto.Cipher import AES
k=binascii.unhexlify('76656E757343544676656E757343544676656E757343544676656E7573435446')
iv = binascii.unhexlify('202cb962ac59075b964b07152d234b70')
c=binascii.unhexlify('a80d5eb43508e549f83e2e254c0a0f0644be58f453baced4af4777c4cd1b7575')
aes = AES.new(k, AES.MODE_CBC, iv)
print aes.decrypt(c)
