#include <stdio.h>

int main() {
    int num, digit, max = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

  
    if(num < 0) {
        num = -num;
    }

    for( num != 0; num /= 10) {
        digit = num % 10;       
        if(digit > max) {
            max = digit;      
        }
    }

    printf("Maximum digit = %d\n", max);

    return 0;
}

