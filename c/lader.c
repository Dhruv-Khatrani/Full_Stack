#include<stdio.h>
#include<stdio.h>


void main()
{
	int marks;
	
	printf("enter your marks :");
	scanf("%d",&marks);
	printf("your marks: %d",marks);
	
	if (marks > 100 || marks < 0){
		printf("\n your marks are in valid : %d ",marks);
	}
	
	else if (marks >=85 && marks <=100 ){
		printf("\n a grade : %d",marks);
	}
	
	else if (marks >=70 && marks <=85  ){
	    printf("\n b gread : %d",marks);
    }
  
    else if (marks >=70 && marks <=50){
    	printf("\n c gread : %d", marks);
	}
	
	else if (marks >=50 && marks <=35){
		printf("\n d gread : %d", marks);
	}
	
	else {
		printf("\n you are faile  %d", marks);
	}
	
	
}
	
