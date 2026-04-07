#include<iostream>
using namespace std;

class load{
	
	public:
		void display(){
			cout<<"\ndisplay function 1 ";
		
		}
		
		void display(int x){
			cout<<"\ndisplay function 2";
			
		}
		void display(int x ,int y){
			cout<<"\ndisplay function 2";
		}
		
};

int main()
{
	load data;
	data.display();
	data.display();
	data.display(10);	
	return 0;
}
