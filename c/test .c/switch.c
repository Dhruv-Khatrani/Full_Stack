#include <stdio.h>
#include <conio.h>

void main()
{
	int day;
	
	printf("enter your day :");
	scanf("%d",&day);
	printf("day : %d",day);
	
	switch(day){
		case 1:
			printf("\n monday :");
			break;
			
		case 2:
			printf("\n tuesday :");
			break;
				
		case 3:
			printf("\n weday :");
			break;
			
			
		case 4:
			printf("\n thuday :");
			break;
			
			
		case 5:
			printf("\n firday :");
			break;
			
			
		case 6:
			printf("\n satday :");
			break;
			
			
		case 7:
			printf("\n sunday :");
			break;
		default :
			printf("\ninvalid");
			
	}
	
	getch();
}
