#-*- coding:utf-8 -*-
from crc32_util import *
#�÷���crc32_reverse(CRC,����,�ַ����ķ�Χ)
crc = [0x9D945A6E]
#char_set=string.letters + string.digits + '_'
#char_set=string.printable
for i in crc:
    crc32_reverse(i, 5, char_set=string.printable)

#password:f~Z-;lapEwF\<0ZkhyAo5