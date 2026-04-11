#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b;
	
	printf("enter your a :");
	scanf("%d",&a);
	printf("a : %d",a);
	
	printf("\nenter your b:");
	scanf("%d",&b);
	printf("b : %d",b);
	
	
	if(a>b){
		printf("\na max : %d",a);
	}
	
	else{
		printf("\nb max : %d",b);
	}
	
	
	
	getch();
}
