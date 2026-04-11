#include <stdio.h>
#include <conio.h>

void main()
{
	int a;
	int b;
	
	printf("enter your a :");
	scanf("%d",&a);
	printf("a :%d",a);
	
	printf("\nenter your b :");
	scanf("%d",&b);
	printf("b : %d",b);
	
	printf("\n-------clc--------");
	printf("\nsum : %d",a+b);
	printf("\nsub : %d",a-b);
	printf("\nmul : %d",a*b);
	printf("\ndiv : %d",a/b);
	
	getch();
	
	
}
