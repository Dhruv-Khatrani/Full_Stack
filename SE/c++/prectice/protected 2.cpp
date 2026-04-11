#include<iostream>
using namespace std;
class prenet{
	protected:
		int money = 500;
		
		public:
		void display(){
			cout<<"\n your money "<<money;
		}
};

class child : public prenet{
	public :
		void data(){
			cout<<"\n your money"<<money;	
		}
};

int main()
{
	child obj;
	obj.data();
	
	return 0;
}
