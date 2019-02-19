#include <string.h>
#include <stdio.h>
#include "sm4.h"

int main()
{
	unsigned char key[16] = {0xDA,0x98,0xF1,0xDA,0x31,0x2A,0xB7,0x53,0xA5,0x70,0x3A,0x0B,0xFD,0x29,0x0D,0xD6};
	unsigned char input[16] = {0x66,0x6c,0x61,0x67,0x7b,0x65,0x34,0x34,0x33,0x35,0x33,0x34,0x31,0x2d,0x34,0x30};
	unsigned char output[16]={0xc7,0xbc,0xa4,0xf4,0xac,0x18,0x62,0x39,0xca,0xd1,0xcb,0x2d,0x79,0x7c,0x14,0xc3};
	unsigned char input2[16] = {0xc7,0xbc,0xa4,0xf4,0xac,0x18,0x62,0x39,0xca,0xd1,0xcb,0x2d,0x79,0x7c,0x14,0xc3};
	unsigned char output2[16] = {0};
	unsigned char iv[]={'\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00'};
	sm4_context ctx;
	unsigned long i;

	//encrypt standard testing vector
	printf("----encrypt testing----\n");
	sm4_setkey_enc(&ctx,key);
	sm4_crypt_ecb(&ctx,1,16,input,output);
	for(i=0;i<16;i++)
		printf("%02x ", output[i]);
	printf("\n");

	//decrypt testing
	printf("----decrypt testing----\n");
	sm4_setkey_dec(&ctx,key);
	sm4_crypt_ecb(&ctx,0,16,output,output);
	for(i=0;i<16;i++)
		printf("%02x ", output[i]);
	printf("\n");

	//encrypt standard testing vector mode cbc
	// printf("----cbc mode encrypt testing----\n");
	// sm4_setkey_enc(&ctx,key);
	// sm4_crypt_cbc(&ctx,1,16,iv,input,output);
	// for(i=0;i<16;i++)
	// 	printf("%02x ", output[i]);
	// printf("\n");

	//decrypt testing mode cbc
	// printf("----cbc mode decrypt testing----\n");
	// sm4_context ctx4;
	// sm4_setkey_dec(&ctx4,key);
	// sm4_crypt_cbc(&ctx4,0,16,iv,input2,output2);
	// for(i=0;i<16;i++)
	// 	printf("%02x ", output2[i]);
	// printf("\n");
	
    return 0;
}
