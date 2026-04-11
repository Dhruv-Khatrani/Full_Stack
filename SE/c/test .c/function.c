

#include<stdio.h>
#include<conio.h>

// function outside main
void demo(){
	printf("\nHello demo function\n");
}

void LineData(){
	int a;
	for(a=1;a<=20;a++){
		printf("*");
	}
}

void main()
{
	LineData();
	demo();
	LineData();
	printf("\nHello dhruv\n");
	LineData();
	
	getch();
}

