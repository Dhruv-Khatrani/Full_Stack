#include<stdio.h>
#include<conio.h>

void main(){
	
	int a[3][3],i,j;
	int b[3][3],sub [3][3];
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			
			
			printf("enter element = ",i,j);
			scanf("%d",&a[i][j]);
		    
		}
		
	}
	
	printf("-----3d a array-----\n");
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("\na[%d][%d] : %d",i,j,a[i][j]);
		}
	}
	
	printf ("\n");
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			
			
			printf("\nenter element = ",i,j);
			scanf("%d",&b[i][j]);
		    
		}
		
	}
	
	printf("-------3d b array------");
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("\nb[%d][%d] : %d",i,j,b[i][j]);
		}
	}
	
	printf("-------- sum array----------");
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			
				sub [i][j] = a[i][j] - b[i][j];
				
 				
			
			
		}
	}
	
		for(i=0;i<3;i++){
		   for(j=0;j<3;j++){
			printf("\nsub[%d][%d] : %d",i,j,b[i][j]);
		}
	}
	
	getch();
}
