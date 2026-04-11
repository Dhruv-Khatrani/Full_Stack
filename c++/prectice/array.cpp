#include<iostream>
using namespace std;

int main ()
{
	
	int a[5],i;
	
	
	for(i=0;i<5;i++){
		cout<<"\n enter your element :";
		cin>>a[i];
	}
	
	for(i=0;i<5;i++){
		cout<<"\na["<<i<<"]"<<a[i];
		
	}
	
	cout<<"\n";
	
	return 0;
}
