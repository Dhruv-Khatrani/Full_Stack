#include<iostream>
#include<cstring>
using namespace std;


class student {
	private :
		int rollno;
		char name[50];
		
		public:
			student(){
				cout<<"\nenter your rollno :";
				cin>>rollno;
				cout<<"\nenter your name :";
				cin>>name;
			}
		
		student(int r,const char s[50]){
			rollno = r;
			strcpy(name,s);
		}
		
		void display(){
			cout<<"\nrollno :"<<rollno;
			cout<<"\nname :"<<name;
		}
};




int main()
{
	student s1;
	s1.display();
	
	student s2(3,"dhruv");
	s2.display();
	
	return 0;
}
