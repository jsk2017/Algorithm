

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

    // printf("------ DES CBC MODE ------- \n");

    // //128 bits
    // uint8_t data3[]="Attack at dawn!!";
    // int len3 = 16;
    // uint8_t key3[]="Sixteen byte key";
    // uint8_t iv0[] = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00";
    // aes_encrypt_cbc(AES_CYPHER_128, data3, len3, key3,iv0);

    // printf("E 128 bits: 0x");
    // for(uint8_t i=0;i<len3;i++){
    //     printf("%02x",data3[i]);
    // }
    // printf("\n");


    return 0;
}


