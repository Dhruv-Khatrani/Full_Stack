#include<stdio.h>
#include<conio.h>

void main ()
{
	int i,j;
	char count;
	
	for(i=5;i>=1;i--){
		for(j=1; j<=i;j++) {
			printf("%d",count);
			count++;
		}
		printf("\n");
	}
	
	
	getch();
}
