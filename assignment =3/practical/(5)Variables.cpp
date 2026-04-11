#include <iostream>
using namespace std;

int main()
{
    
    int a = 10, b = 5;        
    float x = 5.5, y = 2.5;     
    char grade = 'A';           
    string name = "Dhruv";      

    const float PI = 3.14;

    int sum = a + b;
    int product = a * b;
    float division = x / y;

    cout << "Name: " << name << endl;
    cout << "Grade: " << grade << endl;

    cout << "\nInteger Operations:" << endl;
    cout << "Sum = " << sum << endl;
    cout << "Product = " << product << endl;

    cout << "\nFloat Division:" << endl;
    cout << "x / y = " << division << endl;

    cout << "\nConstant Value:" << endl;
    cout << "PI = " << PI << endl;

    return 0;
}
