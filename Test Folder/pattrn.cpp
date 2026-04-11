#include<iostream>
using namespace std;

int main()
{
	int r,c;
	
	
	int num = 1;
//	char demo = 'A';
	
	for(r=1;r<=5;r++){
		for(c=1;c<=r;c++){
			cout<<num<<" ";
			num++;
		}
		cout<<"\n";
	}

	
	
	return 0;
}
