
#include<stdio.h>
#include<conio.h>

void main()
{
	int a[5];
	int i,j ;
	int temp;
	
	for(i=0;i<5;i++){
		printf("enter your element :");
		scanf("%d",&a[i]);
	}
	
	printf("\n --------store the element-------- ");
	
	for(i=0;i<=4;i++){
		printf("\na[%d] : %d",i,a[i]);
	}
	
	
	printf("\n---- Ascdeing A Element ----");

    for(i=0;i<5;i++){
    	for(j=i+1;j<5;j++){
    		if(a[i] > a[j]){
    			temp = a[i];
    			a[i] = a[j];
    			a[j] = temp;
			}
		}
	}
	
	for(i=0;i<=4;i++){
		printf("\na[%d] : %d",i,a[i]);
}

    printf("\n -----descding a element-----");
    
    for(i=0;i<5;i++){
    	for(j=i+1;j<5;j++){
    		if(a[i] < a[j]){
    			temp = a[i];
    			a[i] = a[j];
    			a[j] = temp;
			}
		}
	}

    for(i=0;i<5;i++){
    	printf("\na[%d] : %d",i,a[i]);
	}
 
	getch();
}





