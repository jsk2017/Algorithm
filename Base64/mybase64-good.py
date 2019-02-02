# -*- coding:utf-8 -*-
#decode base64
decode="YnBpYW4gdOhlAO1vbmtleSJhbmQgYnBhZOxleSJ0aOUga2lua2Nqb3UgYXBlAOZyaWVuZPE="
table='''IJKLMNOPABCDEFGHQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'''
# print len(table)
# x="".join(map(lambda x:bin(table.index(x))[2:].zfill(6),decode))#zfillÓÃÓÚÌî³ä
# print x
# appen=len(x)%8
# for ap in range(8-appen):
# 	x+='0'
# print len(x)%8
# # print x
# res=[]
# for i in range((len(x))/8):
# 	res.append(chr(eval('0b'+x[i*8:(i+1)*8])))
# print "".join(res)

# #encode base64
# en=[]
# encode=[]
# m="qxDYs0TOBKX2zvHurdfhv3vNsg1YvZw9"
# for d in list(m):
# 	en.append(bin(ord(d))[2:].zfill(8))
# enc="".join(en)
# appen=len(enc)%6
# for ap in range(6-appen):
# 	enc+='0'
# print enc
# for i in range((len(enc))/6):
# 	encode.append(table[eval('0b'+enc[i*6:(i+1)*6])])
# print "".join(encode)



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
print mydecodeb64(decode)