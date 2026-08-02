 #include <stdio.h>

int main() {
    int num, first, last, temp;

    printf("Enter a number: ");
    scanf("%d", &num);

    // Get last digit
    last = num % 10;

    temp = num;
    while (temp >= 10) {
        temp = temp / 10;
    }
    first = temp;

    // Sum of first and last digit
    int sum = first + last;

    printf("Sum of first and last digit: %d\n", sum);

    return 0;
}

