#include <iostream>
using namespace std;

float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    if (b == 0) {
        cout << "Error! Division by zero is not allowed." << endl;
        return 0;
    }
    return a / b;
}

int main() {
    float num1, num2;
    int choice;

    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    cout << "\nChoose operation:\n";
    cout << "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n";
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    switch(choice) {
        case 1:
            cout << "Result = " << add(num1, num2);
            break;
        case 2:
            cout << "Result = " << subtract(num1, num2);
            break;
        case 3:
            cout << "Result = " << multiply(num1, num2);
            break;
        case 4:
            cout << "Result = " << divide(num1, num2);
            break;
        default:
            cout << "Invalid choice!";
    }

    return 0;
}
