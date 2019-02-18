/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "IDEA.h"

void usage()
{
	printf("Usage: IDEA [-e(encrypt)|-d(decrypt)]/n");
}

void encrypt()
{
	uint16_t key[8];
	uint64_t plaintext[1024], ciphertext[1024];
	char str[1024];
	int block_cnt = 0, i = 0, len;
	printf("/ninput plaintext(in hex):");
	scanf("%s", str);
	len = strlen(str);
	for(; len%16 != 0; len++)//fill the text with '0' such that it can be cut into 64-bit blocks.
		str[len] = '0';
	str[len] = '/0';
	
	while(sscanf(str+block_cnt*16, "%016llx", &(plaintext[block_cnt]))!=EOF)//4x16=64
		block_cnt++;
	
	/*while(sscanf(str+block_cnt*4, "%04hx", &(tmp[block_cnt]))!=EOF)
		block_cnt++;
	for(i = 0; i*4 < block_cnt; i++)
	{
		plaintext[i] = tmp[i*4];
		for(j = 1; j < 4; j++)
			plaintext[i] = (plaintext[i]<<16)|tmp[i*4+j];
	}
	block_cnt /= 4;*/
	
	printf("/ninput 128-bit secret key(in hex):");
	scanf("%s", str);
	len = strlen(str);
	if(len > 32)
	{
		printf("/nsecret key too long");
		return ;
	}
	for(; len < 32; len++)
		str[len] = '0';
	str[len] = '/0';
	
	for(i = 0; i < 8; i++)
		sscanf(str+i*4, "%04hx", &key[i]);

	printf("/nciphertext = ");
	for(i = 0; i < block_cnt; i++)
	{
		idea_encrypt(plaintext[i], key, &(ciphertext[i]));
		printf("%016llx", ciphertext[i]);
	}
	printf("/n");
}

void decrypt()
{
	uint16_t key[8];
	uint64_t plaintext[1024], ciphertext[1024];
	char str[1024];
	int block_cnt = 0, i = 0, len;
	printf("/ninput ciphertext(in hex):");
	scanf("%s", str);
	len = strlen(str);
	for(; len%16 != 0; len++)
		str[len] = '0';
	str[len] = '/0';
	
	while(sscanf(str+block_cnt*16, "%016llx", &(ciphertext[block_cnt]))!=EOF)
		block_cnt++;
	/*while(sscanf(str+block_cnt*4, "%04hx", &(tmp[block_cnt]))!=EOF)
		block_cnt++;
	for(i = 0; i*4 < block_cnt; i++)
	{
		ciphertext[i] = tmp[i*4];
		for(j = 1; j < 4; j++)
			ciphertext[i] = (ciphertext[i]<<16)|tmp[i*4+j];
	}
	block_cnt /= 4;*/
	
	printf("/ninput 128-bit secret key(in hex):");
	scanf("%s", str);
	len = strlen(str);
	if(len > 32)
	{
		printf("/nsecret key too long");
		return ;
	}
	for(; len < 32; len++)
		str[len] = '0';
	str[len] = '/0';
	
	for(i = 0; i < 8; i++)
		sscanf(str+i*4, "%04hx", &key[i]);

	printf("/nplaintext = ");
	for(i = 0; i < block_cnt; i++)
	{
		idea_decrypt(ciphertext[i], key, &(plaintext[i]));
		printf("%016llx", plaintext[i]);
	}
	printf("/n");
}

int main(int argc, char **argv)
{
	if(argc < 2)
	{
		usage();
		return 1;
	}
	if(argv[1][0] != '-')
	{
		usage();
		return 1;
	}
	switch(argv[1][1])
	{
		case 'e':
		case 'E': 
			encrypt();
			break;
		case 'd':
		case 'D':
			decrypt();
			break;
		default:
			usage();
			return 1;
	}
	return 0;
}
