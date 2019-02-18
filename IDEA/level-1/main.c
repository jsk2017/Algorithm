#include <stdio.h>
#include <string.h>
#include "IDEA.h"

int main(void){
    uint16_t key[8] = {0x1234,0x5678,0x90ab,0x3456,0x5678,0x2345,0x1908,0x1235};
	uint64_t plaintext[] = {0x1234567898765432};
	int block_cnt = 0, i = 0, len;
    uint64_t ciphertext[1024]={0};

    idea_encrypt(plaintext[i], key, ciphertext);
    printf("0x%016llx\n", ciphertext[0]);

    idea_decrypt(ciphertext[0], key, &(plaintext[i])); 
    printf("0x%016llx\n", plaintext[0]);
    
}