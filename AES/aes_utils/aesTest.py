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
    # 如果是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果是被加密字符串或长度不足的密码，则确保其长度为16的整数倍
    else:
        if len(str)%16 != 0:
            zerocount = 16-len(str) % 16
            for i in range(0, zerocount):
                str = str + '\0'
        return str
# ECB模式加密
def encrypt_ECB1(str, key):
    # 补全字符串
    str = align(str)
    print len(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# ECB模式解密
def decrypt_ECB1(str, key):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 解密
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