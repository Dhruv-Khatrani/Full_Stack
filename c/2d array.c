#include<stdio.h>
#include<conio.h>

void main()
{
	int a [2] [2] ,i,j;
	
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("enter element %d : row %d :col :-",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	
	printf(" -----2d array------\n");
	
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("\n[%d][%d] : %d",i,j,a[i][j]);
		}
	}
	
	getch();
	
}
