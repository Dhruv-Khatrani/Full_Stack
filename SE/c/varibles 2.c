#include<stdio.h>
#include<conio.h>


void main()
{

   float a;
   float b;
   
   printf("enter a number a:");
   scanf("%f",&a);
   printf("a: %.2f",a);
   
   printf("\nenter a number b:");
   scanf("%f",&b);
   printf("b: %.2f",b);

   float sum;
   sum = a+b;
   
   printf("\nsum %f",sum);

}
