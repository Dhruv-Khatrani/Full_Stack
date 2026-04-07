#include <stdio.h>
#include <conio.h>

void main()
{
	int marks;
	
	printf("enter your marks :");
	scanf("%d",&marks);
	printf("marks : %d ",marks);
	
	if(marks >100 || marks < 0){
		printf("\nmarks is invalid : %d",marks);
	}
	else if(marks >=85 && marks<=100){
		printf("\n a grad : %d",marks );
	} 
	else if(marks >=70 && marks<85){
		printf("\n b grad : %d",marks);
	}
	else if (marks >=50 && marks <70){
		printf("\n c grad : %d",marks);
	}
	else if (marks >=33 && marks <50){
		printf("\n d grad : %d",marks);
	}
	
	else{
		printf("\n fell : %d ",marks);
	}
	getch();
}
