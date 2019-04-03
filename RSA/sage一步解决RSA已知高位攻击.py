from sage.all import *
import binascii
n =	  0x73204217f728a2fb7dc798618f23c5796675eee1ccd60a3a7be9cddf7d0eb30e9b004b0246051fcbc26ce99b67e23f07d3f2a493b1194af2777ffdfd5d66c61ba4fa2cd14536010ee00e695863039829c315c594c84170559822fcceb20afdc56a81ab7105e17efb0afd8f090bce2e5330e1c78e2e3ab26a1f49610b49b0fafa75b342b5c1a79322be4a92fac102958ed43aee787c221ea5c23e9485321c6b901cdb5c584bebcbea644a8f2c40bfbaf2dee40102e660e37d41b1f2ccee933a57693ee8ee2473bec98911ccd4b853704c7ed73b86da962845efe5399561fb3b0c37f5f0e730ddebcea7144351064f1ee04c1348125807a760186ac33316633d09
 
 
cipher = 0x52ab2147297ac1e695ba664352b637892607a66aeea0224980dddc2dfa964a238b9ff67d5e2f25cde03b5a8859eb1c809241d425f923dcb583e6f5ae7e6a2024fb37e3da9b417ea6a6091702a4d695e6e61cf70b8e5e2c1f343fc4b79758e86482706c6ca1a782b3cc4958dcd1be5e3162079204b44321432775c266c0c3deed6b23416842277acc909eb50e2af919e02e5319bfaaa0d25f2399d24ec299d4901fdaf460d6ee402241df39374423e2450fec11b757cf531dd2ccabf60d22607e0017ed4803f6591580d0d767013aec3ee48bda2ae8e94a1c3886457bd4364162fb235c18ca508502827a1a5f6ac2c4759a01acf6cf939aeeaeeb155ca48db4d8
 
e2 = 0x10001
pbits = 1024
for i in range(0,127):
	p4=0x9904bce5f97920383ddc58aa477490a76bb731382b7af3154c5606298e0dde77bebeb66a0285b362c987fb16b5b8d1e237205e3847eaa7b2a89e058e080506e253be3ec5aa76a7a6
	p4=p4+int(hex(i),16)
	#print hex(p4)
	kbits = pbits - p4.nbits()	#未知需要爆破的比特位数
	print p4.nbits()
	p4 = p4 << kbits
	PR.<x> = PolynomialRing(Zmod(n))
	f = x + p4
	roots = f.small_roots(X=2^kbits, beta=0.4) #进行爆破
	#rint roots
	if roots:		  #爆破成功，求根
		p = p4+int(roots[0])
		print "p: ", hex(int(p))
		assert n % p == 0
		q = n/int(p)
		print "q: ", hex(int(q))
		print gcd(p,q)
		phin = (p-1)*(q-1)
		#print gcd(e2,phin)
		d = inverse_mod(e2,phin)
		flag = pow(cipher,d,n)
		flag = hex(int(flag))[2:-1]
		print binascii.unhexlify(flag)
		break