from Crypto.Cipher import DES

# ECB 
# iv = 'qwertyui'
key = '12345678'
modoul = DES.new(key,DES.MODE_ECB)
plain = 'qwertyui'
ciphertext = modoul.encrypt(plain)

for a in ciphertext:
    print hex(ord(a))
# a = ciphertext
# print ciphertext

# CBC

# key = '12345678'
# iv = '\x00'*8
# modoul = DES.new(key,DES.MODE_CBC,iv)
# plain = 'qwertyui'
# ciphertext = modoul.encrypt(plain)

# b = ciphertext
# print ciphertext

# if a == b:
#     print "equal"

# CFB

# key = '12345678'
# iv = '\x00'*8
# modoul = DES.new(key,DES.MODE_CFB,iv)
# plain = 'qwertyui'
# ciphertext = modoul.encrypt(plain)

# c = ciphertext
# print ciphertext

# if c == b:
#     print "equal"