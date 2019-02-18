

#include "rijndael.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

uint64_t main(void){

    // aes_encrypt_ecb(AES_CYPHER_T mode, uint8_t *data, int len, uint8_t *key);
    printf("------ DES ECB MODE ------- \n");
    //128 bits
    uint8_t data[]="Attack at dawn!!";
    int len = 16;
    uint8_t key[]="Sixteen byte key";
    aes_encrypt_ecb(AES_CYPHER_128, data, len, key);

    printf("E 128 bits: 0x");
    for(uint8_t i=0;i<len;i++){
        printf("%02x",data[i]);
    }
    printf("\n");

    printf("D 128 bits: ");
    aes_decrypt_ecb(AES_CYPHER_128,data,len,key);
    printf("%s\n",data);

    //192 bits
    uint8_t data1[]="Attack at dawn!!";
    int len1 = 16;
    uint8_t key1[]="Sixteen byte key12345678";
    aes_encrypt_ecb(AES_CYPHER_192, data1, len1, key1);

    printf("E 192 bits: 0x");
    for(uint8_t i=0;i<len1;i++){
        printf("%02x",data1[i]);
    }
    printf("\n");


    //256 bits
    uint8_t data2[]="Attack at dawn!!";
    int len2 = 16;
    uint8_t key2[]="Sixteen byte key1234567812345678";
    aes_encrypt_ecb(AES_CYPHER_256, data2, len2, key2);

    printf("E 256 bits: 0x");
    for(uint8_t i=0;i<len2;i++){
        printf("%02x",data2[i]);
    }
    printf("\n");

    printf("------ DES CBC MODE ------- \n");

    //128 bits
    uint8_t data3[]="Attack at dawn!!";
    int len3 = 16;
    uint8_t key3[]="Sixteen byte key";
    uint8_t iv0[] = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00";
    aes_encrypt_cbc(AES_CYPHER_128, data3, len3, key3,iv0);

    printf("E 128 bits: 0x");
    for(uint8_t i=0;i<len3;i++){
        printf("%02x",data3[i]);
    }
    printf("\n");

    //192 bits
    uint8_t data4[]="Attack at dawn!!";
    int len4 = 16;
    uint8_t key4[]="Sixteen byte key12345678";
    uint8_t iv1[] = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00";
    aes_encrypt_cbc(AES_CYPHER_192, data4, len4, key4,iv1);

    printf("E 192 bits: 0x");
    for(uint8_t i=0;i<len4;i++){
        printf("%02x",data4[i]);
    }
    printf("\n");


    //256 bits
    uint8_t data5[]="Attack at dawn!!";
    int len5 = 16;
    uint8_t key5[]="Sixteen byte key1234567812345678";
    uint8_t iv2[] = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00";
    aes_encrypt_cbc(AES_CYPHER_256, data5, len5, key5,iv2);

    printf("E 256 bits: 0x");
    for(uint8_t i=0;i<len5;i++){
        printf("%02x",data5[i]);
    }
    printf("\n");

    return 0;
}


