#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

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

/*将大写字母转换成小写字母*/  
int tolower(int c)  
{  
    if (c >= 'A' && c <= 'Z')  
    {  
        return c + 'a' - 'A';  
    }  
    else  
    {  
        return c;  
    }  
} 

//将十六进制的字符串转换成整数  
int htoi(char s[])  
{  
    int i = 0;  
    int n = 0;  
    if (s[0] == '0' && (s[1]=='x' || s[1]=='X'))  
    {  
        i = 2;  
    }  
    else  
    {  
        i = 0;  
    }  
    for (; (s[i] >= '0' && s[i] <= '9') || (s[i] >= 'a' && s[i] <= 'z') || (s[i] >='A' && s[i] <= 'Z');++i)  
    {  
        if (tolower(s[i]) > '9')  
        {  
            n = 16 * n + (10 + tolower(s[i]) - 'a');  
        }  
        else  
        {  
            n = 16 * n + (tolower(s[i]) - '0');  
        }  
    }  
    return n;  
} 

void reverse(char *s, int start, int end)
{ 
    char t; 
    while(end>start){
        t=s[start]; 
        s[start]=s[end]; 
        s[end]=t;
        start++; 
        end--; 
    }  
}

int main()
{
    uint32_t v[2]={1,2},k[4]={2,2,3,4};
    // v为要加密的数据是两个32位无符号整数
    // k为加密解密密钥，为4个32位无符号整数，即密钥长度为128位
    int flagLen = 0;
    bool success = false;
    char flag[33];
    memset(flag, 0, sizeof(flag));//清空字符串
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);

    printf("Please input you flag:");
    flagLen = getStr(flag,32);

    //check formant
    uint8_t vv[5] = {0};
    strncpy(vv,flag,4);
    uint8_t five = 123;
    uint8_t last = 125;
    uint8_t *v1,*v2;
    if(((uint8_t)flag[5] - five)>0){
        printf("five error!");
        return -1;
    }

    if(((uint8_t)flag[flagLen-1] + last) == 250){
        ;
    }else{
        printf("last error!");
        return -1;
    }

    if(strcmp(vv,"flag")){
        printf("header error!");
        return -1;
    }
    int mallocSize = flagLen - 6;
    char *tokstr = (char *)malloc(sizeof(char)*mallocSize+1);
    memset(tokstr, 0, sizeof(tokstr));//清空字符串
    strncpy(tokstr,flag+5,mallocSize);

    v1 = strtok(tokstr,"-");

    v2 = strtok(NULL,"-");

    //exchange scale
    uint32_t flagLong[2];
    flagLong[0] = (uint32_t)htoi((char *)v1);
    flagLong[1] = (uint32_t)htoi((char *)v2);
    // printf("%d",sizeof(int));  4 byte == 32 bit
    
    // printf("加密前原始数据：%x %x\n",flagLong[0],flagLong[1]);
    encrypt(flagLong, k);
    // printf("加密后的数据：%x %x\n",flagLong[0],flagLong[1]);

    // check flag
    uint8_t check_enc[4];
    uint8_t check_index[4] = {3,1,0,2};
    uint8_t i=0;
    check_enc[0] = 0x5;
    check_enc[1] = 0xd7;
    check_enc[2] = 0xb8;
    check_enc[3] = 0x67;
    for(i=0;i<4;i++){
        uint8_t t = (uint8_t)(flagLong[0]>>(8*i));
        // printf("%x\t",t);
        if(check_enc[i]!=flagLong[check_index[i]]){
            success = false;
        }
    }

    char check_enc_last[9] = "3c471c36";
    // snprintf(check_enc_last,9,"%x",flagLong[1]);//63c174c3
    reverse(check_enc_last,0,7);
    uint32_t enc_hex = htoi(check_enc_last);

    // printf("%x",enc_hex);
    if(flagLong[1] == enc_hex){
        success = true;
    }
    if(!success){
        printf("You Lost!\n");
    }else{
        printf("You Win!\n");
    }
    return 0;
}
