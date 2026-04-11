#include<iostream>
using namespace std;

class Student{
	private : 
		int money = 500;
		public:
			void display(){
				cout<<"\nYour money : "<<money;
			}
};

class Emp: public Student{
	public:
		void data(){
			cout<<"\nEmp Money : "<<money;
		}
};

int main(){
	
	return 0;
}
