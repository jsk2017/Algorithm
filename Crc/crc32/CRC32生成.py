#-*- coding:utf-8 -*-
#crc32校验码生成 
#根据chunk_type和chunk_data
import binascii

def _crc(v):y
	return '0x%x' % (binascii.crc32(v) & 0xffffffff)

chunk_type="49484452"
chunk_data="0000029c000001dd0806000000"
chunk_old_crc="FE1A5AB6"
chunk_crc=(chunk_type+chunk_data).decode("hex")
print _crc(chunk_crc)
