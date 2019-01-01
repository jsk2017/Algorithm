#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>
#include<stdlib.h>
#include <stdio.h>
#include <string.h>


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

void Hex2Str( const char *sSrc,  char *sDest, int nSrcLen )  
{  
    int  i;  
    char szTmp[3];  
  
    for( i = 0; i < nSrcLen; i++ )  
    {  
        sprintf( szTmp, "%02X", (unsigned char) sSrc[i] );  
        memcpy( &sDest[i * 2], szTmp, 2 );  
    }  
    return ;  
}  

int getStr(char *buffer,int maxLen){
    char c;  // 读取到的一个字符
    int len = 0;  // 当前输入的字符串的长度
    // 一次读取一个字符，保存到buffer
    // 直到遇到换行符(\n)，或者长度超过maxLen时，停止读取
    while( (c=getchar()) != '\n' ){
        buffer[len++]=c;  // 将读取到的字符保存到buffer
        if(len>=maxLen){
            break;
        }
    }
    buffer[len]='\0';  // 读取结束，在末尾手动添加字符串结束标志
    fflush(stdin);  // 刷新输入缓冲区
    return len;
}

int main(int argc,char ** argv){
    
    char enc[23]  = {232, 86, 8, 28, 69, 57, 192, 153, 1, 33, 226, 253, 141, 89, 30, 212, 29, 94, 84, 46, 230, 190, 249};
    uint8_t s[256] = {0}; //S-box
    uint8_t flagLen = 0,j=0,i;
    uint8_t success = true;
    char key[9] = "BadRer00";
    char flag[24];
    // uint8_t flag[] = "flag{rC4_0Llv2_1s_Ea3Y}";
    memset(flag, 0, sizeof(flag));//清空字符串

    printf("Please input you flag:\n");
    flagLen = getStr(flag,23);

    for(i=0;i<23;i++){
        enc[i] = enc[i]^(i+0x31);
    }

    rc4_init(s,(uint8_t *)key, strlen(key)); //初始化密钥
    rc4_crypt(s,(uint8_t *)flag,strlen(flag));//加密

    //加密后的flag同enc进行比较
    // Hex2Str( (const char *)flag,  sDest, keyLen );

    // for(i=flagLen-1;i>=0;i--){
    //     if(enc[i]==flag[i]){
    //         j++;
    //     }
    // }
    // if(j==23){
    //     success = true;
    // }

    if(success){
        printf("flag is :%s\n",flag);
    }else{
        printf("Please try again!\n");
    }

    return 0;

}

/*
key内置 base64
程序加密过程
base64 解密 key
输入flag
rc4 + key 加密 flag
解密密文
最后同 解密后的密文 比较 如果相同则正确输出


解题过程
分析（静态或者动调）得到 key
同样动调得到 最后比较的 密文
最后就是RC4解密
*/
