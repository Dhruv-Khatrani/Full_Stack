#include<stdio.h>
#include<conio.h>

void main ()
{
	
	char operator;
	int num1;
	int num2;
	int result;
	
	
	printf("enter the operator (+,-,*,/ ):");
	scanf("%d",&operator);
 
 
     printf("enter two number :");
     scanf("%d %d",&num1,num2);
     
     
     switch(operator){
     	
     	case '+' :
		   result = num1+num2;
		   printf("%d +%d = %d\n",num1,num2,result);
		   break;   
		   
		case '-':
		result = num1-num2;
		printf("%d - %d=%d\n",num1,num2,result);
		break;
		
		case '*' :
		result =num1*num2;
		printf("%d*%d=%d\n",num1,num2,result);
		break;
		
		case '/' :
			if(num2!=0){
			
			result =num1/num2;
			printf("%d / %d=%d\n",num1,num2,result);
	}  else {
		printf("error : division by zero not allowed\n");
	}
		break;
		
		
		default :
		
			printf("\nerror");
		}	
		
		
		     	
     	
     	
	 
	
	
}
 
