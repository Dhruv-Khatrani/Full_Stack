#include<stdio.h>
#include<conio.h>


void main()
{
	int a[5];
	int i,j;
	int temp;
	
	for (i=0;i<5;i++){
		printf("enter your value :");
		scanf("%d",&a[i]);
		
		printf("\n stor the value");
		
	}
	for (i=0;i<5;i++){
		printf("\n[%d] : %d ",i,a[i]);
	}
	
	
	printf("\n ----- ascdeing a value ---------");
	
	
	for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			
			if(a[i]>a[j]){
			
			
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		    }
			
		}
	}
	for (i=0;i<5;i++){
		printf("\n[%d]: %d",i,a[i]);
	}
	   
	printf("\n ------- descdeing a value--------");
	
		for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			
			if(a[i]<a[j]){
			
			
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		    }
			
		}
	}
	for (i=0;i<5;i++){
		printf("\n[%d]: %d",i,a[i]);
	}
	   
	
	
	getch();
}
