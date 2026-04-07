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
				cout<<"\nenter your name1 :";
				cin>>name1;
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
	
	student dhruv;
	dhruv.putdata();
	dhruv.getdata();
	
	
	
	return 0;
}
