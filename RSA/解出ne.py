from Crypto.PublicKey import RSA 
pub = RSA.importKey(open('warmup.pub').read())
n = long(pub.n)
e = long(pub.e)
print 'n:%d'%n
print 'e:%d'%e