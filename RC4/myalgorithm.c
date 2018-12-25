#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>
#include<stdlib.h>
#include <stdio.h>
#include <string.h>
#include"myalgorithm.h"


void rc4_init(uint8_t *s, uint8_t *key, uint16_t Len) //初始化函数
{
    int i =0, j = 0;
    char k[256] = {0};
    uint8_t tmp = 0;
    for (i=0;i<256;i++) {
        s[i] = i;
        k[i] = key[i%Len];
    }
    for (i=0; i<256; i++) {
        j=(j+s[i]+k[i])%256;
        tmp = s[i];
        s[i] = s[j]; //交换s[i]和s[j]
        s[j] = tmp;
    }
 }

void rc4_crypt(uint8_t *s, uint8_t *Data, uint16_t Len) //加解密
{
    int i = 0, j = 0, t = 0;
    uint16_t k = 0;
    uint8_t tmp;
    for(k=0;k<Len;k++) {
        i=(i+1)%256;
        j=(j+s[i])%256;
        tmp = s[i];
        s[i] = s[j]; //交换s[x]和s[y]
        s[j] = tmp;
        t=(s[i]+s[j])%256;
        Data[k] ^= s[t];
     }
} 
