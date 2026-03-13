#include<iostream>
using namespace std; 

int main()
{
	int a,b,c;
	
	cout<<"enter your a number : ";
	cin>>a;
	cout<<"a :"<<a;
	
	cout<<"\nenter your b number :";
	cin>>b;
	cout<<"b :"<<b;
	
	cout<<"\nenter your c number :";
	cin>>c;
	cout<<"c :"<<c;
	
	
	if(a>b && a>c){
		cout<<"\n a is max "<<a;
	}
	else if (b>c){
		cout<<"\n b is max "<<b;
	}
	else {
		cout<<"\n c is max "<<c;
	}
	
	return 0; 
}
