#include <iostream>
using namespace std;

int main()
{
	float length, width, area;
	
	cout<<"enter your length :";
	cin>>length;
	
	cout<<"enter your width :";
	cin>>width;
	
	area = length * width;
	
	cout<<"Area of rectangle = "<< area;
	
	
	
	return 0;
}


#include <iostream>
using namespace std;

class rectangle
{
 private :
    float langth,width;
	
	public :
	   void getdata()
	   {
	   
	      cout<<"enter langth";
	      cin>>langth;
	      
	      cout<<"enter width";
	      cin>> width;
	 }
	 
	 float calculaarea()
	 {
	 	return langth * width;
	 }
	      
		
	
};


int main()
{
	rectangel rect;
	rect.grtdata();
	cout << "Area of rectangle = " << rect.calculateArea();
	return 0;
}
