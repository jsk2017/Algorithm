# -*- coding:utf-8 -*-
#参数p为568位 差576 8位，即两个16进制字符
n = 0x65025c6c787775a3854316ec6c88ac541e7f0ac9f265a880ad878e8647c56c643d0f0b98ea54dc23fdf97934c8c4851a3ab744c8794893f25555aa69e79691ba7487e5d2d2e0593344f7ae6938f87baf37760749dabd7d7078dc0dd93725faae0e82195b9bcc45489035462320248183cdb5d36ec7fabc7a15cce2350c0011b138bec7dc9105759e1664fb0f0c3cc5d851e337369d10342e33a9c00ec185088a7e04500bd330b98e2e6fe533cad6192be98172d93521cbcaaae5439a968d425cfe152ec3a6600e88de8875b5b8e2a6417eda01e4a50ba027c409dc9862fb9de1a2cbc15f23753ea5f4676eb9e5da9d3017c9c4502c5762bf1a4f1e6924233565
p = 0x8c7b80575a50e2aca16bb9cb56e3494e8ddffe6b4d2dca09a201a367b04127a0f2f2dea7c3c8ad7e5f66d9a87f4c9a8bb05159af644e67344ae27daa4924b1f5bf0caa23c6b3979
import string
dic = string.digits + "abcdef"

for a in dic:
    for b in dic:
        pp = hex(p) + a + b
        #p需要用0补全到1024位
        pp += '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        #要加的数字与补全p时0的个数有关
        pp = int(pp, 16)
        p_fake = pp+0x10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        pbits = 1024
        kbits = pbits-576
        pbar = p_fake & (2^pbits-2^kbits)
        print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)
        PR.<x> = PolynomialRing(Zmod(n))
        f = x + pbar
        try:
            x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.4
            print x0 + pbar
        except:
            pass