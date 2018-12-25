import base64

enc = [0xd9, 0x64, 0x3b, 0x28, 0x70, 0xf, 0xf7, 0xa1, 0x38, 0x1b, 0xd9, 0xc1, 0xb0, 0x67, 0x21, 0x94, 0x5c, 0x1c, 0x17, 0x6a, 0xa3, 0xf8, 0xbe]
xor_data = [i+0x31 for i in range(23)]
result_enc = []
for i in range(23):
        result_enc.append((xor_data[i]^enc[i]))
print (result_enc)

DEFAULT_KEY = ""
def rc4(data, key=DEFAULT_KEY, skip=1024):
    x = 0
    box = range(256)
    
	

    x = 0
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        tmp = box[i]
        tmp2 = box[x]
        box[i] = box[x]
        box[x] = tmp
    

    x = 0
    y = 0
    out = []
    if skip > 0:
        for i in range(skip):
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
	
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        k = box[(box[x] + box[y]) % 256]
        # print k
        out.append(hex(ord(char) ^ k))

    # return ''.join(out)
    print len(out)
    return out

if __name__ == '__main__':
    # handle input file or stream
    import sys
    
    # print rc4("flag{test_flag_for_rc4}", "QweaSdzx", 0)