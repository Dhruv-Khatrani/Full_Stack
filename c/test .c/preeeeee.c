#include<stdio.h>
#include<conio.h>

void main()
{
   int r,c;
   char count =0;
   
   for(r=1;r<=4;r++){
   	for(c=1;c<=r;c++){
   		count++;
   		printf("%d",count);
	   }
	   
	   printf("\n");
   }
	
	getch();
}
