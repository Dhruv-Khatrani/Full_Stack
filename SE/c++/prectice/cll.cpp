#include <iostream>
using namespace std;

// Base class
class A {
public:
    void showA() {
        cout << "Class A\n";
    }
};

// Derived from A (Single Inheritance)
class B : public A {
public:
    void showB() {
        cout << "Class B\n";
    }
};

// Derived from A (Hierarchical Inheritance)
class C : public A {
public:
    void showC() {
        cout << "Class C\n";
    }
};


int main() {
    C obj;
    obj.showA();
    obj.showC();
    
    B data;
    data.showB();
    data.showA();

    // obj.showA(); ? Ambiguity (comes from both B and C)
    
    return 0;
}
