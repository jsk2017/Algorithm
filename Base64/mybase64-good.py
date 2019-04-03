# -*- coding:utf-8 -*-
import base64 
decode="YnBpYW4gdOhlAO1vbmtleSJhbmQgYnBhZOxleSJ0aOUga2lua2Nqb3UgYXBlAOZyaWVuZPE="
table='''IJKLMNOPABCDEFGHQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'''

def mydecodeb64(enc):
	enc=enc.replace("=","")
	x="".join(map(lambda x:bin(table.index(x))[2:].zfill(6),enc))#zfillÓÃÓÚÌî³ä
	# print x
	for ap in range(8-(len(x)%8)):
		x+='0'
	# print x
	plain=[]
	for i in range((len(x))/8):
		plain.append(chr(eval('0b'+x[i*8:(i+1)*8])))
	return "".join(plain).replace("\x00","")
def myencodeb64(plain):
	en=[]
	encode=[]
	for d in list(plain):
		en.append(bin(ord(d))[2:].zfill(8))
	plain="".join(en)
	for ap in range(6-(len(plain)%6)):
		plain+='0'
	# print enc
	for i in range((len(plain))/6):
		encode.append(table[eval('0b'+plain[i*6:(i+1)*6])])
	return "".join(encode)

# another base64


def self_base64(s,flag):
	from string import  maketrans
	import base64 
	fr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	to = 'ABCyVPGHTJKLMNOFQRSIUEWDYZgbc8sfah1jklmnopqret5v0xX9wi234u67dz+/'
	trans = maketrans(fr,to)
	if flag == 1:#dec
		res = base64.b64decode(s.translate(trans))
	elif flag == 0:#enc
		res = base64.b64encode(s.translate(trans))

	return res


s = "bWzXZSB3b3JrTHRvTGRvTQ=="
print self_base64(s,1)