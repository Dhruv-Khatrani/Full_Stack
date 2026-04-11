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


class C : public A{
	int c;
		public: 
		void putC(){
			cout<<"\nEnter c : ";
			cin>>c;
		}
		void getC(){
			cout<<"\nYour C : "<<c;
		}
};



int main()
{
	 B data;
	 data.getA();
	 data.putA();
	 data.putB();
	 data.getB();
	 
	 C obj;
	 obj.putA();
	 obj.getA();
	 obj.putC();
	 obj.getC();
	
	
	return 0;
}
