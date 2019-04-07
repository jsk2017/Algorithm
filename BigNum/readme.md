大数运算 算法

别人的代码，例子。

主要实现思路用字符数组来表示大数，然后采用合适的算法，模拟手工运算。
加减法：
https://blog.csdn.net/gd007he/article/details/68958798

```
1 //#include"big.h"
  2 //将整个加法写成一个方法，然后在main函数中调用。
  3 #include<stdlib.h>
  4 #include<stdio.h>
  5 #include<string.h>
  6 char * bigadd(char *adda,int lena,char *addb,int lenb){     //加法运算的方法。
  7   int num='0',i,k,j,tmp;
  8   for(i=0;i<lena;i++){                                      //将字符编码的数字转换为对应的数，
  9       adda[i]=adda[i]-num;                                  //例如6实际在字符串中存储的是54，
 10   }                                                         //减去0对应的48得到真实的6存储在字符数组中。
 11   for(i=0;i<lenb;i++){
 12       addb[i]=addb[i]-num;
 13   }
 14     int lensum;                                             //求出结果数组的长度。
 15     lensum = lena>lenb?lena:lenb;
 16     lensum++;
 17     char *result,final[BUFSIZ];                             //result用于返回结果集，final数组用于整理结果集。
 18     result=(char*)calloc(lensum,1);
 19     for(i=0,j=0;i<lena&&j<lenb;i++,j++){                    //循环的给每一位作加法
 20       result[i]=adda[lena-i-1]+addb[lenb-i-1];
 21     }
 22     if(lena>lenb){                                          //使用判断将较大数的高位也写入结果数组
 23       for(i=lenb;i<lena;i++){
 24          result[i]=adda[lena-i-1];
 25       }
 26     }
 27     if(lenb>lena){
 28       for(i=lena;i<lenb;i++){
 29          result[i]=addb[lenb-i-1];
 30       }
 31     }
 32     for(k=0;k<lensum-1;k++){                                //整理结果数组的每一位，满10进一。
 33       if(result[k]>9){
 34          tmp=result[k]/10;
 35          result[k]=result[k]%10;
 36          result[k+1] += tmp;
 37       }
 38     }
 39    j=0;
 40    if(result[lensum-1]!=0){                                 //去掉前前导0将结果处理后写到final数组中。
 41       final[j]=result[lensum-1]+'0';
       j++;
 43    }
 44    for(i=lensum-2;i>=0;i--){
 45       final[j++]=result[i]+'0';
 46    }
 47    result=final;                                            //再把result指针指向final数组中，并返回result指针。    
 48    return result;
 49 }
 50 int main(){                                                 //利用main测试方法，用puts打印结果。               
 51    int lena,lenb;
 52    char *result,sa[BUFSIZ],sb[BUFSIZ];
 53    scanf("%s",sa);
 54    scanf("%s",sb);
 55    lena=strlen(sa);
 56    lenb=strlen(sb);
 57    result=bigadd(sa,lena,sb,lenb);
 58    puts(result);
 59 
 60 }


```

https://blog.csdn.net/gd007he/article/details/68961974

```
//#include"big.h"
  2 #include<stdlib.h>
  3 #include<stdio.h>
  4 #include<string.h>
  5 char * bigsub(char *suba,int lena,char *subb,int lenb){  //大数减法的的方法。
  6   int lensum,num='0';
  7   int i,j,k,tmp;
  8   lensum=lena>lenb?lena:lenb;
  9   for(i=0;i<lena;i++){                                   //将ASCII编码的数字转换为真正的数字存储，便于计算。
 10       suba[i]=suba[i]-num;                               //大数加法注释中有例子。
 11   }
 12   for(i=0;i<lenb;i++){
 13       subb[i]=subb[i]-num;
 14   }
 15     char *result,final[BUFSIZ];
 16     result=(char*)calloc(lensum,1);                      //动态分配内存空间，在大数加法中忘记介绍
 17     for(i=0,j=0;i<lena&&j<lenb;i++,j++){                 //calloc()有两个参数，本次会分配 ‘lensum’ 个大小为 ‘1’ 字节的内存空间
 18       result[i]=suba[lena-i-1]-subb[lenb-i-1];           //并且全部初始化为0，返回指向内存的指针
 19     }
 20     if(lena>lenb){                        //判断，并将高位写入result结果数组中。
 21       for(i=lenb;i<lena;i++){
 22          result[i]=suba[lena-i-1];
 23       }
 24     }
 25     if(lenb>lena){                        //由于只允许大减小所以这个判断可以删除。
 26       for(i=lena;i<lenb;i++){
 27          result[i]=subb[lenb-i-1];
 28       }
 29     }
 30     for(k=0;k<lensum-1;k++){              //整理结果，同大数加法类似，只是判断方法变了而已。
 31       if(result[k]<0){
 32          result[k]=result[k]+10;
 33          result[k+1] -=1;
 34       }
 35     }
 36     j=0;
 37     if(result[lensum-1]!=0){             //将结果集去除前导0后整理到final数组中。
 38       final[j]=result[lensum-1]+num;
 39       j++;
 40     }
 41     for(i=lensum-2;i>=0;i--){
 42       final[j++]=result[i]+num;
 43 
 44     }
 45     result=final;                        //将指针指向final数组并返回数组的指针。
 46     return result;
 47 }
 48 int main(){                                                 //利用main测试方法，用puts打印结果。               
 49    int lena,lenb;
 50    char *result,sa[BUFSIZ],sb[BUFSIZ];
 51    scanf("%s",sa);
 52    scanf("%s",sb);
 53    lena=strlen(sa);
 54    lenb=strlen(sb);
 55    result=bigsub(sa,lena,sb,lenb);
 56    puts(result);
 57 
 58 } 
版权声明：本文为博主原创文章，转载请附上博文链接！
```


乘除法：

https://blog.csdn.net/gd007he/article/details/69055031

————————


其他大数运算库，可以参考这篇文章。文中所说的，有些虽然不是专门做大数运算的库，不过都是相关的库。

gmp 可以参考下 http://www.cnblogs.com/ECJTUACM-873284962/p/8350320.html

```

Crypto++：https://github.com/weidai11/cryptopp

MIRACL：https://github.com/CertiVox/MIRACL

GNU MP：https://gmplib.org/

Piologie： http://www.hipilib.de/pidownload.htm

cryptlib：http://www.cs.auckland.ac.nz/~pgut001/cryptlib/

RSAEuro：http://www.rsaeuro.com/products/RSAEuro/

OpenSSL：http://www.openssl.org/

RSARef：http://download.gale.org/rsaref20.tar.Z

```