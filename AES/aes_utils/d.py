# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex

def align(str, isKey=False):
	if isKey:
		if len(str) > 16:
			return str[0:16]
		else:
			return align(str)
	else:
		if len(str)%16 != 0:
			zerocount = 16-len(str) % 16
			for i in range(0, zerocount):
				str = str + '\0'
		return str

def encrypt_ECB(str, key):
	str = align(str)
	print len(str)
	key = align(key, True)
	AESCipher = AES.new(key, AES.MODE_ECB)
	cipher = AESCipher.encrypt(str)
	return b2a_hex(cipher)

def decrypt_ECB(str, key):
	key = align(key, True)
	AESCipher = AES.new(key, AES.MODE_ECB)
	paint = AESCipher.decrypt(a2b_hex(str))
	return paint

def str2hex(aa):
	ss=''
	for j in xrange(len(aa)):
		tmp=hex(ord(aa[j]))[2:]
		if len(tmp)==1:
			tmp='0'+tmp
		ss+=tmp
	return ss

def jiemi2(str):
	s='f8c49056e4ccf9a11e090eaf471f418d'
	s2=''
	for i in xrange(16,len(str)):
	# print miwen[i]
		s2+=chr(ord(str[i])^ord(s[i%32]))

	return s2

key1 = 'f8c49056e4ccf9a1'
key2 = '1e090eaf471f418d'

def main():
	fo=open("flag.jpg.lock",'rb')
	# miwen=fo.read()
	s='f8c49056e4ccf9a11e090eaf471f418d'
	aaa=0
	zzz=''
	a=open("de.jpg",'wb')
	for i in xrange(10000):
		v24 = ord(s[i&0x1f])
		#aaa+=v24   
		miwen = fo.read(v24)
		aa=miwen[:16]
	
		ss=str2hex(aa)
		if not (v24&0x1):
			s1 = decrypt_ECB(ss, key1)
		else:
			s1 = decrypt_ECB(ss, key2)
		if len(s1)<16:
			s1+=chr(0)*(16-len(s1))
		a.write(s1)
		s2 = jiemi2(miwen)
		a.write(s2)
		if len(miwen)<1:
			break
	a.close()


if __name__ == '__main__':
	# ss="e1136bb9bd1a7c5f35767ea30e93e4bd"
	# s1 = decrypt_ECB(ss, key1)
	# print len(s1)
	main()
