#include<iostream>
using namespace std;

int main()
{
	int a,b,c;
	
	cout<<"enter your a :";
	cin>>a;
	cout<<"a  :"<<a;
	
	cout<<"\n enter your b :";
	cin>>b;
	cout<<"b :"<<b;
	
	cout<<"\n enter your c :";
	cin>>c;
	cout<<"c :"<<c;
	
	if(a>b && a>c){
		cout<<"\na is max "<<a;
	} 
	
	else if(b>c){
		cout<<"\nb is max "<<b;
	}
	
	else{
		cout<<"\nc is max "<<c;
	}
	
	
	return 0;
}
