#-*- coding:utf-8 -*-
#加密函数，如果text不是16的倍数 加密文本text必须为16的倍数！，那就补足为16的倍数
#这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用  
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex
# 补全字符
def align(str, isKey=False):
    # 如果是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果是被加密字符串或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str

# ECB模式加密
def encrypt_ECB(str, key):
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# ECB模式解密
def decrypt_ECB(str, key):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.rstrip('\0')
    return paint

# CBC模式加密
def encrypt_CBC(str, key,iv):
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES，引入初始向量
    AESCipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# CBC模式解密
def decrypt_CBC(str, key,iv):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.rstrip('\0')
    return paint

# CFB模式加密
def encrypt_CFB(str, key,iv):
    # 补全字符串，虽然明文长度没有限制，但是密码仍然需要16位
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# CFB模式解密
def decrypt_CFB(str, key,iv):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CFB, iv)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.rstrip('\0')
    return paint

# OFB模式加密
def encrypt_OFB(str, key,iv):
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_OFB, iv)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# OFB模式解密
def decrypt_OFB(str, key,iv):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_OFB, iv)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.rstrip('\0')
    return paint
def aes_test():
	# 先设置一段明文和密码
	Text = 'Suprise！！****** *****r!'
	key = 'mor'
	iv="1234567890123456"


	# ECB模式加密
	ciphertext = encrypt_ECB(Text, key)
	print ("ECB模式密文：" + ciphertext)
	# ECB模式解密
	plaintext = decrypt_ECB(ciphertext, key)
	print ("ECB模式明文：" + plaintext)


	# CBC模式加密
	ciphertext = encrypt_CBC(Text, key,iv)
	print ("CBC模式密文：" + ciphertext)
	# CBC模式解密
	plaintext = decrypt_CBC(ciphertext, key,iv)
	print ("CBC模式明文：" + plaintext)


	# CFB模式加密
	ciphertext = encrypt_CFB(Text, key,iv)
	print ("CFB模式密文：" + ciphertext)
	# CFB模式解密
	plaintext = decrypt_CFB(ciphertext, key,iv)
	print ("CFB模式明文：" + plaintext)

	# OFB模式加密
	ciphertext = encrypt_OFB(Text, key,iv)
	print ("OFB模式密文：" + ciphertext)
	# OFB模式解密
	plaintext = decrypt_OFB(ciphertext, key,iv)
	print ("OFB模式明文：" + plaintext)
