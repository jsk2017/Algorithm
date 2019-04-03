from sets import Set
import operator
 
with open('aes-192cipher.txt','r') as f:
    output = f.read()
 
uniques=dict([])
 
for i in xrange(len(output)/32):
    word=output[32*i:32*i+32]
    if uniques.has_key(word):
        uniques[word]+=1
    else:
        uniques[word]=0
print len(uniques)
print uniques
for (block,c) in zip(uniques,map(chr, list(xrange(ord('A'), ord('Z')+1)) + list([ord(' ')]))):
    output=output.replace(block,c)
fp=open("out.txt","w")
fp.write(output)