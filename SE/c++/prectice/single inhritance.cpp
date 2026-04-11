#include<iostream>
using namespace std;

class a{
	private :
	int a;
	
	public:
		
		void puta(){
			cout<<"\n enter your a :";
			cin>>a;
		}
		
		void geta(){
			cout<<"\nyour a :"<<a;
		}
			
 };
 
 class b : public a{
 	
 	int b;
 	
 	public:
 		void putb(){
 			cout<<"\nenter your b :";
 			cin>>b;
		 }
		 
		 void getb(){
		 	cout<<"\nb :"<<b;
		 }
 };

int main()
{
	b obj;
	obj.putb();
	obj.getb();
	
	obj.puta();
	obj.geta();
	return 0;
}
