# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex
from aes_util import *

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
def encrypt_ECB1(str, key):
    str = align(str)
    print len(str)
    key = align(key, True)
    AESCipher = AES.new(key, AES.MODE_ECB)
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)
def str2hex(aa):
	ss=''
	for j in xrange(len(aa)):
		tmp=hex(ord(aa[j]))[2:]
		if len(tmp)==1:
			tmp='0'+tmp
		ss+=tmp
	return ss
def decrypt_ECB1(str, key):
    key = align(key, True)
    AESCipher = AES.new(key, AES.MODE_ECB)
    paint = AESCipher.decrypt(a2b_hex(str))
    return paint
def dec_xor_data(cipher):
	plain=[]
	for i in range(16,len(cipher)):
		temp=chr(ord(cipher[i]) ^ ord(akey[i%32]))
		plain.append(temp)
	return "".join(plain)
akey="f8c49056e4ccf9a11e090eaf471f418d"
dword_5FA3C00C=[0x66,0x38,0x63,0x34,0x39,0x30,0x35,0x36,0x65,0x34,0x63,0x63,0x66,0x39,0x61,0x31,0x31,0x65,0x30,0x39,0x30,0x65,0x61,0x66,034,0x37,0x31,0x66,0x34,0x31,0x38,0x64]
def main():
	#从文件中读取
	fp_enc=open("flag.jpg.lock","rb")
	fp_dec=open("de.jpg","wb")
	i=0
	while 1:
		#v24=dword_5FA3C00C[i&0x1f]
		v24 = ord(akey[i&0x1f])
		cipher=fp_enc.read(v24)
		cipher_aes=str2hex(cipher[:16])
		if not (v24&0x1):
			hkey=akey[:16]
			plain_aes=decrypt_ECB1(cipher_aes,hkey)
		else:
			hkey=akey[16:]
			plain_aes=decrypt_ECB1(cipher_aes,hkey)
		if len(plain_aes) < 16:
			plain_aes+=chr(0)*(16-len(plain_aes))
		fp_dec.write(plain_aes)
		plain_xor=dec_xor_data(cipher)
		fp_dec.write(plain_xor)
		i=i+1
		if len(cipher)<1:
			break
	fp_dec.close()	
	
if __name__=="__main__":
	main()