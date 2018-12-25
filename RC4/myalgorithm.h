#ifndef __H__MYALGORITHM
#define __H__MYALGORITHM
#include<stdint.h>
#include<stdbool.h>
#include<stdlib.h>

void rc4_init(uint8_t *s, uint8_t *key, uint16_t Len);//初始化函数

void rc4_crypt(uint8_t *s, uint8_t *Data, uint16_t Len);//加解密

#endif