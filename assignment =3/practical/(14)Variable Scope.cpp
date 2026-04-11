#include <iostream>
using namespace std;

int x = 10;

void showLocal() {
    int x = 20; 
    cout << "Inside showLocal(), local x = " << x << endl;
}

void modifyGlobal() {
    x = x + 5; 
    cout << "Inside modifyGlobal(), global x = " << x << endl;
}

int main() {
    cout << "In main(), global x = " << x << endl;

    showLocal();  
    modifyGlobal();

    cout << "Back in main(), global x = " << x << endl;

    return 0;
}
