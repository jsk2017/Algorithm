#include <stdio.h>
#include <stdint.h>
 
//加密函数
void encrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0=v[0], v1=v[1], sum=0, i;           /* set up */
    uint32_t delta=0x9e3779b9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i < 32; i++) {                       /* basic cycle start */
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

//解密函数
void decrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0=v[0], v1=v[1], sum=0xC6EF3720, i;  /* set up */
    uint32_t delta=0x9e3779b9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i<32; i++) {                         /* basic cycle start */
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

int main()
{
    uint32_t v[2]={1,2},k[4]={2,2,3,4};
    // v为要加密的数据是两个32位无符号整数
    // k为加密解密密钥，为4个32位无符号整数，即密钥长度为128位
    printf("加密前原始数据：%u %u\n",v[0],v[1]);
    encrypt(v, k);
    printf("加密后的数据：%u %u\n",v[0],v[1]);
    decrypt(v, k);
    printf("解密后的数据：%u %u\n",v[0],v[1]);
    return 0;
}

/*
出题思路

要求输入flag格式flag{*-*}
编写flag格式验证代码。
编写取出 v0 和 v1 的代码 并进行类型转换
生成flag
验证程序是否实现其功能
验证解题思路是否符合逻辑。

程序功能：
获取flag
验证flag格式 flag长度为6+1+8+8
按照格式要求 取出 v0 和 v1 如 E01a345b
key 内置 
Tea加密
同固定数据进行比较

解题思路：
动态调试，看懂flag格式验证的策略。
根据数据特征识别算法
动调 dump 出 key 和最后的 enc
编写解密脚本 得到 plain
根据格式要求代入程序进行验证

*/