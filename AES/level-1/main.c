

#include "rijndael.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

uint64_t main(void){

    // aes_encrypt_ecb(AES_CYPHER_T mode, uint8_t *data, int len, uint8_t *key);
    uint8_t data[]="Attack at dawn!!";
    int len = 16;
    uint8_t key[]="Sixteen byte key";
    aes_encrypt_ecb(AES_CYPHER_128, data, len, key);
    
    printf("E: 0x");
    for(uint8_t i=0;i<len;i++){
        printf("%x  ",data[i]);
    }
    


    return 0;
}


