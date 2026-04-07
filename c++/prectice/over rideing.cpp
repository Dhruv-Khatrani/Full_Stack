#include<iostream>
using namespace std;

class pernet{
	public:
		void display(){
			cout<<"\nclass is pernet";
		}
};
class child : public pernet{
	public :
		void display(){
			cout<<"\nclass is child";
		}
};
int main()
{
	child data;
	data.display();
	
	data.pernet::display();
	data.display();
	data.display();
	return 0;
}
