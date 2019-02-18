from Crypto.Cipher import AES
from Crypto import Random
from libnum import n2s,s2n

print "-----Des ECB mode-------"
# ECB 128

key = b'Sixteen byte key' # 16 bytes
cipher = AES.new(key,AES.MODE_ECB)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 128 bits: '+hex(s2n(plain))
decode = cipher.decrypt(plain)
print 'D 128 bits: '+decode

# ECB 192

key = b'Sixteen byte key12345678' # 24 bytes
cipher = AES.new(key,AES.MODE_ECB)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 192 bits: '+hex(s2n(plain))

# ECB 256

key = b'Sixteen byte key1234567812345678' # 32 bytes
cipher = AES.new(key,AES.MODE_ECB)
print 'E 256 bits: '+hex(s2n(plain))


print "-----Des CBC mode-------"
# CFB 128
key = b'Sixteen byte key' # 16 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CBC,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 128 bits: '+hex(s2n(plain))


# CFB 192

key = b'Sixteen byte key12345678' # 24 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CBC,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 192 bits: '+hex(s2n(plain))

# CFB 256

key = b'Sixteen byte key1234567812345678' # 32 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CBC,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 256 bits: '+hex(s2n(plain))


print "-----Des CFB mode-------"
# CFB 128
key = b'Sixteen byte key' # 16 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CFB,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 128 bits: '+hex(s2n(plain))

# CFB 192

key = b'Sixteen byte key12345678' # 24 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CFB,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 192 bits: '+hex(s2n(plain))

# CFB 256

key = b'Sixteen byte key1234567812345678' # 32 bytes
iv = '\x00'*16
cipher = AES.new(key,AES.MODE_CFB,iv)
plain = cipher.encrypt('Attack at dawn!!')
print 'E 256 bits: '+hex(s2n(plain))


'''c
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')
'''