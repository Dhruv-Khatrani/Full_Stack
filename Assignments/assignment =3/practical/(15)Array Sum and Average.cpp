#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;

    int arr[n];  
    int sum = 0;
    double average;

    cout << "Enter " << n << " integers:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    average = static_cast<double>(sum) / n;

    cout << "Sum of array elements = " << sum << endl;
    cout << "Average of array elements = " << average << endl;

    return 0;
}
