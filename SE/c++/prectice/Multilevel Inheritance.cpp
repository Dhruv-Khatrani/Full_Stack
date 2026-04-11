#include<iostream>
using namespace std;

class a{
	
	public:
		void getdata(){
			cout<<"\n a class";
		}
};

class b{
	public:
		void getdatb(){
			cout<<"\n b class";
		}
};

class c : public a,public b{
	public:
		void getdatc(){
			cout<<"\n c class";
		}
};

int main()
{
	c obj;
	obj.getdata();
	obj.getdatb();
	obj.getdatc();
	
	return 0;
}

