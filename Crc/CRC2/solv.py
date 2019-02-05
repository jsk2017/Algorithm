mem = map(chr,[0x42, 0x4D, 0x96, 0x02, 0x36, 0x28, 0x32, 0x04, 0x01, 0x18, 0x60, 0x02, 0xE7, 0xBF, 0xC8, 0xC8, 0xE0, 0xDD, 0xF2, 0xFF, 0xC8, 0xE0, 0xDD, 0x24, 0x1C, 0xED, 0xC8, 0xE0, 0xDD, 0xCC, 0x48, 0x3F, 0xE8, 0xA2, 0x57, 0x7A, 0xB9, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x1D, 0xE6, 0xB5, 0xCC, 0x48, 0x3F, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x4C, 0xB1, 0x22, 0x7F, 0x7F, 0x7F, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xF2, 0xFF, 0x4C, 0xB1, 0x22, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xCC, 0x48, 0x3F, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x7F, 0x7F, 0x7F, 0x24, 0x1C, 0xED, 0xCC, 0x48, 0x3F, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x24, 0x1C, 0xED, 0x27, 0x7F, 0xFF, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x1D, 0xE6, 0xB5, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x9A, 0x76, 0x83, 0xC8, 0xE0, 0xDD, 0x57, 0x7A, 0xB9, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x4C, 0xB1, 0x22, 0xE8, 0xA2, 0x24, 0x1C, 0xED, 0xC9, 0xAE, 0xFF, 0x24, 0x1C, 0xED, 0xCC, 0x48, 0x3F, 0xC8, 0xE0, 0xDD, 0x4C, 0xB1, 0x22, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x24, 0x1C, 0xED, 0xC8, 0xE0, 0xDD, 0x27, 0x7F, 0xFF, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC9, 0xAE, 0xFF, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0xC8, 0xE0, 0xDD, 0x57, 0x7A, 0xB9, 0xC8, 0xE0, 0xDD, 0x24, 0x1C, 0xED, 0xC8, 0xE0, 0xDD, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

from crc64 import crc64


def print_mat(m):
   for k in [''.join([str(i) for i in m[j]]) for j in xrange(len(m))]:
       print k

def print_mat2(m):
   print '{'
   for l in m:
       line = 'bitset<91>{"'
       for i in l[:-1]:
           if i:
               line+='1'
           else:
               line+='0'
       if l[-1]:
           line+='1"},'
       else:
           line+='0"},'
       print line
   print '}'

def print_vec(v):
   line = '{"'
   for i in v[:-1]:
       if i:
           line += '1'
       else:
           line += '0'
   if v[-1]:
       line += '1"}'
   else:
       line += '0"}'
   print line


base = crc64(mem)
ac_base = 0x676F5F675F695F6C ^ base
ac_base_bits = [(ac_base >> i) & 1 for i in xrange(64)]
ac_base_bits += [1]

bits_pos = []
for i in xrange(13):
   for bit in xrange(7):
       pos = 0x14 * i
       changed_byte = chr(ord(mem[pos]) ^ (1 << bit))
       bits_pos.append((pos, bit, base ^ crc64(mem[:pos] + [changed_byte] + mem[pos+1:])))

mat = [[None] * 91 for i in xrange(65)]
for i in xrange(64):
   for j in xrange(91):
       mat[i][j] = (bits_pos[j][2] >> i) & 1

for i in xrange(91):
    if i % 7 == 0:
        mat[64][i] = 1
    else:
        mat[64][i] = 0

def xor(a, b):
   return map(lambda x, y: x ^ y, a, b)


def inner(a, b):
   return reduce(lambda x, y: x ^ y, map(lambda x, y: x & y, a, b))

def rank(m, v):
   w = len(m[0])
   h = len(m)
   last_i = -1

   for j in xrange(w):
       last_i += 1
       if last_i == h:
           break
       for i in xrange(last_i, h):
           if m[i][j] == 1:
               break
       if m[i][j] == 0:
           continue
       i0 = i
       if i0 != last_i:
           m[i0], m[last_i] = m[last_i], m[i0]
           v[i0], v[last_i] = v[last_i], v[i0]
           i0 = last_i
       for i in xrange(i0 + 1, h):
           if m[i][j] == 1:
               m[i] = xor(m[i], m[i0])
               v[i] = v[i] ^ v[i0]

rank(mat, ac_base_bits)
print_mat2(mat)
print_vec(ac_base_bits)