# -*- coding:utf-8 -*-
import gmpy2
from libnum import n2s,s2n
p = gmpy2.mpz(275127860351348928173285174381581152299)
q = gmpy2.mpz(319576316814478949870590164193048041239)
N=gmpy2.mpz(87924348264132406875276140514499937145050893665602592992418171647042491658461)
fp=open("flag.enc","r").read()
cipher=gmpy2.mpz(s2n(fp))
# 计算yp和yq
yp = gmpy2.invert(p,q)
yq = gmpy2.invert(q,p)

# 计算mp和mq
mp = pow(cipher, (p + 1) / 4, p)
mq = pow(cipher, (q + 1) / 4, q)

# 计算a,b,c,d
a = (yp * p * mq + yq * q * mp) % N
b = N - int(a)
c = (yp * p * mq - yq * q * mp) % N
d = N - int(c)

for i in (a,b,c,d):
    s = '%x' % i
    if len(s) % 2 != 0:
        s = '0' + s
    print s.decode('hex')