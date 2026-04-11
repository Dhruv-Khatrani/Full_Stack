#include<iostream>
using namespace std;

class parent{
	protected :
		int money = 500;
		public : 
		void data(){
			cout<<"\nyour money"<<money;
		}
};

class child : public parent{


    public :
    	void demo(){
    		cout<<"\nchild money"<<money;
		}
    
};

int main()
{
	child obj;
	obj.demo();
	
	return 0;
}
