#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define DELTA 0x9e3779b9
#define MX (((z>>5^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))
  
void btea(uint32_t *v, int n, uint32_t const key[4]) {
    uint32_t y, z, sum;
    unsigned p, rounds, e;
    if (n > 1) {          /* Coding Part */
        rounds = 6 + 52/n;
        sum = 0;
        z = v[n-1];
        do {
        sum += DELTA;
        e = (sum >> 2) & 3;
        for (p=0; p<n-1; p++) {
            y = v[p+1]; 
            z = v[p] += MX;
        }
        y = v[0];
        z = v[n-1] += MX;
        } while (--rounds);
    } else if (n < -1) {  /* Decoding Part */
        n = -n;
        rounds = 6 + 52/n;
        sum = rounds*DELTA;
        y = v[0];
        do {
        e = (sum >> 2) & 3;
        for (p=n-1; p>0; p--) {
            z = v[p-1];
            y = v[p] -= MX;
        }
        z = v[n-1];
        y = v[0] -= MX;
        sum -= DELTA;
        } while (--rounds);
    }
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
    // flagLong[2] = (uint32_t)htoi("12345678");
    // printf("%d",sizeof(int));  4 byte == 32 bit
    
    // printf("加密前原始数据：%x %x %x\n",flagLong[0],flagLong[1],flagLong[2]);
    btea(flagLong,2, k);
    // printf("加密后的数据：%x %x %x\n",flagLong[0],flagLong[1],flagLong[2]);
    // check flag
    uint8_t check_enc[4];
    uint8_t check_index[4] = {3,1,0,2};
    uint8_t i=0;
    check_enc[0] = 0x57;
    check_enc[1] = 0x8b;
    check_enc[2] = 0x36;
    check_enc[3] = 0x9b;
    for(i=0;i<4;i++){
        uint8_t t = (uint8_t)(flagLong[0]>>(8*i));
        // printf("%x\t",t);
        if(check_enc[i]!=flagLong[check_index[i]]){
            success = false;
        }
    }

    char check_enc_last[9] = "6b45a63b";
    // snprintf(check_enc_last,9,"%x",flagLong[1]);//b36a54b6
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
