#include<stdio.h>
#include<conio.h>

void main()
{
	int a[5];
	int i;
	
	for(i=0;1<5;i++){
		printf("enter your element");
		scanf("%d",&a[i]);
	}
	
	printf("\n------ store a element--------");
	
	for(i=0;i<=4;i++){
		printf("\na[%d] : %d",i,a[i]);
	}
	
	
	getch();
}
