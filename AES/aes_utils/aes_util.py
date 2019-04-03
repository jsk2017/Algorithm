#-*- coding:utf-8 -*-
#���ܺ��������text����16�ı��� �����ı�text����Ϊ16�ı��������ǾͲ���Ϊ16�ı���
#������Կkey ���ȱ���Ϊ16��AES-128����24��AES-192������32��AES-256��Bytes ����.ĿǰAES-128�㹻��  
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex
# ��ȫ�ַ�
def align(str, isKey=False):
    # ��������룬��Ҫȷ���䳤��Ϊ16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # ����Ǳ������ַ����򳤶Ȳ�������룬��ȷ���䳤��Ϊ16��������
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str

# ECBģʽ����
def encrypt_ECB(str, key):
    # ��ȫ�ַ���
    str = align(str)
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # ����
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# ECBģʽ����
def decrypt_ECB(str, key):
    # ��ȫ�ַ���
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # ����
    paint = AESCipher.decrypt(a2b_hex(str))
    # ȥ��/0
    paint = paint.rstrip('\0')
    return paint

# CBCģʽ����
def encrypt_CBC(str, key,iv):
    # ��ȫ�ַ���
    str = align(str)
    key = align(key, True)
    # ��ʼ��AES�������ʼ����
    AESCipher = AES.new(key, AES.MODE_CBC, iv)
    # ����
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# CBCģʽ����
def decrypt_CBC(str, key,iv):
    # ��ȫ�ַ���
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_CBC, iv)
    # ����
    paint = AESCipher.decrypt(a2b_hex(str))
    # ȥ��/0
    paint = paint.rstrip('\0')
    return paint

# CFBģʽ����
def encrypt_CFB(str, key,iv):
    # ��ȫ�ַ�������Ȼ���ĳ���û�����ƣ�����������Ȼ��Ҫ16λ
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_CFB, iv)
    # ����
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# CFBģʽ����
def decrypt_CFB(str, key,iv):
    # ��ȫ�ַ���
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_CFB, iv)
    # ����
    paint = AESCipher.decrypt(a2b_hex(str))
    # ȥ��/0
    paint = paint.rstrip('\0')
    return paint

# OFBģʽ����
def encrypt_OFB(str, key,iv):
    # ��ȫ�ַ���
    str = align(str)
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_OFB, iv)
    # ����
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)

# OFBģʽ����
def decrypt_OFB(str, key,iv):
    # ��ȫ�ַ���
    key = align(key, True)
    # ��ʼ��AES
    AESCipher = AES.new(key, AES.MODE_OFB, iv)
    # ����
    paint = AESCipher.decrypt(a2b_hex(str))
    # ȥ��/0
    paint = paint.rstrip('\0')
    return paint
def aes_test():
	# ������һ�����ĺ�����
	Text = 'Suprise����****** *****r!'
	key = 'mor'
	iv="1234567890123456"


	# ECBģʽ����
	ciphertext = encrypt_ECB(Text, key)
	print ("ECBģʽ���ģ�" + ciphertext)
	# ECBģʽ����
	plaintext = decrypt_ECB(ciphertext, key)
	print ("ECBģʽ���ģ�" + plaintext)


	# CBCģʽ����
	ciphertext = encrypt_CBC(Text, key,iv)
	print ("CBCģʽ���ģ�" + ciphertext)
	# CBCģʽ����
	plaintext = decrypt_CBC(ciphertext, key,iv)
	print ("CBCģʽ���ģ�" + plaintext)


	# CFBģʽ����
	ciphertext = encrypt_CFB(Text, key,iv)
	print ("CFBģʽ���ģ�" + ciphertext)
	# CFBģʽ����
	plaintext = decrypt_CFB(ciphertext, key,iv)
	print ("CFBģʽ���ģ�" + plaintext)

	# OFBģʽ����
	ciphertext = encrypt_OFB(Text, key,iv)
	print ("OFBģʽ���ģ�" + ciphertext)
	# OFBģʽ����
	plaintext = decrypt_OFB(ciphertext, key,iv)
	print ("OFBģʽ���ģ�" + plaintext)
