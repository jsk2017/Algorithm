#-*- coding:utf-8 -*-
from aes_util import *
from Crypto.Cipher import AES
import binascii
from libnum import n2s,s2n
#useage:
#aes_test()
#encrypt_ECB(Text, key)
#decrypt_ECB(ciphertext, key)
#encrypt_CBC(Text, key,iv)
#decrypt_CBC(ciphertext, key,iv)
#encrypt_CFB(Text, key,iv)
#decrypt_CFB(ciphertext, key,iv)
#encrypt_OFB(Text, key,iv)
#decrypt_OFB(ciphertext, key,iv)
def align(str, isKey=False):
    # ��������룬��Ҫȷ���䳤��Ϊ16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # ����Ǳ������ַ����򳤶Ȳ�������룬��ȷ���䳤��Ϊ16��������
    else:
        if len(str)%16 != 0:
            zerocount = 16-len(str) % 16
            for i in range(0, zerocount):
                str = str + '\0'
        return str
# ECBģʽ����
def encrypt_ECB1(str, key):
    # ��ȫ�ַ���
    str = align(str)
    print len(str)
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # ����
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# ECBģʽ����
def decrypt_ECB1(str, key):
    # ��ȫ�ַ���
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # ����
    paint = AESCipher.decrypt(a2b_hex(str))
    return paint
# p=open("IMG_20180107_093509.jpg.lock.jpg","rb").read(16)
d=open("test.jpg","rb").read(16)
# print b2a_hex(p)
# cipher=b2a_hex(p)
key="1e090eaf471f418d"
# print b2a_hex(d)
b=encrypt_ECB1(b2a_hex(d),key)
print b
print b2a_hex(b)