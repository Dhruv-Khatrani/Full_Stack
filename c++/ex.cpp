#include<iostream>
using namespace std;

class A {
	public:
		void getA(){
			cout<<"\nA class";
		}
};

class B : public A  {
	public:
		void getB(){
			cout<<"\nB class";
		}
};

class C : public A{
	public:
		void getC(){
			cout<<"\nC class";
		}
};

class D : public B , public C{
	public:
		void getD(){
			cout<<"\nD class";
		}
};

int main()
{
	D obj;

	obj.getB();
	obj.getC();
	obj.getD();
    obj.getA();	
    
		
	return 0;
}

