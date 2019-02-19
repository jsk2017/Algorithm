/*
 * SM4/SMS4 algorithm test programme
 * 2012-4-21
 */

#include <string.h>
#include <stdio.h>
#include "sm4.h"

// c7bca4f4ac186239cad1cb2d797c14c3224bba52295416232d3c8e18a85c84f68d31ab1151d58560f96a3c5c6b329
int main()
{
	unsigned char key[16] = {0xDA,0x98,0xF1,0xDA,0x31,0x2A,0xB7,0x53,0xA5,0x70,0x3A,0x0B,0xFD,0x29,0x0D,0xD6};
	unsigned char input[16] = {0x66,0x6c,0x61,0x67,0x7b,0x65,0x34,0x34,0x33,0x35,0x33,0x34,0x31,0x2d,0x34,0x30};
	unsigned char output[16]={0xc7,0xbc,0xa4,0xf4,0xac,0x18,0x62,0x39,0xca,0xd1,0xcb,0x2d,0x79,0x7c,0x14,0xc3};
	sm4_context ctx;
	unsigned long i;

	//encrypt standard testing vector
	// sm4_setkey_enc(&ctx,key);
	// sm4_crypt_ecb(&ctx,1,16,input,output);
	// for(i=0;i<16;i++)
		// printf("%02x ", output[i]);
	// printf("\n");

	//decrypt testing
	sm4_setkey_dec(&ctx,key);
	sm4_crypt_ecb(&ctx,0,16,output,output);
	for(i=0;i<16;i++)
		printf("%02x ", output[i]);
	printf("\n");

	//decrypt 1M times testing vector based on standards.
	// i = 0;
	// sm4_setkey_enc(&ctx,key);
	// while (i<1000000) 
    // {
		// sm4_crypt_ecb(&ctx,1,16,input,input);
		// i++;
    // }
	// for(i=0;i<16;i++)
		// printf("%02x ", input[i]);
	// printf("\n");
	
    return 0;
}
