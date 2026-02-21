#include<stdio.h>
#include<conio.h>

void main()

{

    int maths;
    int eng;
    int sci;
    
    printf(" enter your maths marks:", maths);
    scanf("%d",&maths);

    printf("\nenter your eng marks :", eng);
    scanf("%d",&eng);
    
    printf("\nenter your sci marks :",sci);
    scanf("%d",&sci);
    
    int avg;
    avg = (maths+eng+sci)/3;
    printf ("\naverage of the marks : %d ",avg );

}
