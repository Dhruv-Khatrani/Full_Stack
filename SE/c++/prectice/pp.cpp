#include<iostream>
#include<cstring>
using namespace std;

class A{
	int a;
	public :
		void puta(){
			cout<<"enter your a :";
			cin>>a;
		}
		void geta(){
			cout<<"\nyour a :"<<a;
		}
};

class B {
	int b;
	public :
		void putb(){
			cout<<"\nenter your b :";
			cin>>b;
		}
		void getb(){
			cout<<"\nyour b :"<<b;
		}
};

class C : public A , public B{
	int c;
	public :
		void putc(){
			cout<<"\nenter your c :";
			cin>>c;
		}
		void getc(){
			cout<<"\nyour c :"<<c;
		}
};

int main()
{
	C obj;
	obj.puta();
	obj.geta();
	obj.putb();
	obj.getb();
	obj.putc();
	obj.getc();
	
	
	return 0;
	
}
