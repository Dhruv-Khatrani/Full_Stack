#include <iostream>
using namespace std;

int main()
{

    int a = 10;
    double b = 3.5;

    double result = a + b;  

    cout << "Implicit Type Conversion:" << endl;
    cout << "a = " << a << ", b = " << b << endl;
    cout << "Result (a + b) = " << result << endl;

    double x = 9.7;
    int y;

    y = (int)x;  

    cout << "\nExplicit Type Conversion:" << endl;
    cout << "Original value of x = " << x << endl;
    cout << "After conversion to int = " << y << endl;

    int p = 5, q = 2;
    double div = (double)p / q;

    cout << "\nExplicit Type Casting in Division:" << endl;
    cout << "p / q = " << div << endl;

    return 0;
}
