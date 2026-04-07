#include<iostream>
using namespace std;
/* 

 *
 * *
 * * *
 * * * *
 * * * * *
 1 
 2 3
 4 5 6
 
*/

int main()
{
	
	int r,c;
//	int num = 1;
	int count =1 ;
	
	for(r=1;r<=4;r++){
		for(c=1;c<=r;c++){
			cout<<count<<" ";
			count++;
		}
		cout<<"\n";
	}

	
	return 0;
}
