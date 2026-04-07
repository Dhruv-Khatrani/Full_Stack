#include<iostream>
using namespace std;

class A{
	
	int a;
	
	public: 
		void putA(){
			cout<<"Enter A : ";
			cin>>a;
		}	
		void getA(){
			cout<<"\nYour A : "<<a;
		}
};

class B : public A{
	int b;
	
	public: 
		void putB(){
			cout<<"\nEnter B : ";
			cin>>b;
		}
		void getB(){
			cout<<"\nYour B : "<<b;
		}
};

class c : public A{
	
	int c;
	public :
		void putc(){
			cout<<"enter your c :";
			cin>>c;
			
		}
		void getc(){
			cout<<"your c :"<<c;
		}
};

int main(){
	b data;
	data.
	
	return 0;
}

