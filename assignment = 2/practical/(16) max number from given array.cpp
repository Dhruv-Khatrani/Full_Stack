#include <stdio.h>

int findMax(int arr[], int n) {
    int max = arr[0]; // Assume first element is max
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int n;
  
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max = findMax(arr, n);

    printf("Maximum number in the array is: %d\n", max);

    return 0;
}

