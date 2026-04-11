#include<iostream>
using namespace std;


class student{
	
	private:
		
		int roolno;
		string name1;
		
		public :
			
			void putdata(){
				cout<<"\nenter your roolno :";
				cin>>roolno;
				cin.ignore();
				cout<<"\nenter your name1 :";
				getline(cin,name1);
			}
			
			void getdata(){
				cout<<"\nyour roolno :"<<roolno;
				cout<<"\nyour name1  :" <<name1;
			}
	
	
};



int main()
{
	student s1;
    s1.putdata();
	s1.getdata();
	
	
	
	
	return 0;
}
