#include <stdio.h>

int main() {

    int num1, num2;

    // Taking input from user
    printf("Enter first integer: ");
    scanf("%d", &num1);

    printf("Enter second integer: ");
    scanf("%d", &num2);

    // Arithmetic Operations
    printf("\n--- Arithmetic Operations ---\n");
    printf("Addition: %d\n", num1 + num2);
    printf("Subtraction: %d\n", num1 - num2);
    printf("Multiplication: %d\n", num1 * num2);

    if (num2 != 0) {
        printf("Division: %d\n", num1 / num2);
        printf("Modulus: %d\n", num1 % num2);
    } else {
        printf("Division and Modulus not possible (division by zero).\n");
    }

    // Relational Operations
    printf("\n--- Relational Operations ---\n");
    printf("num1 == num2 : %d\n", num1 == num2);
    printf("num1 != num2 : %d\n", num1 != num2);
    printf("num1 > num2  : %d\n", num1 > num2);
    printf("num1 < num2  : %d\n", num1 < num2);
    printf("num1 >= num2 : %d\n", num1 >= num2);
    printf("num1 <= num2 : %d\n", num1 <= num2);

    // Logical Operations
    printf("\n--- Logical Operations ---\n");
    printf("(num1 > 0 && num2 > 0) : %d\n", (num1 > 0 && num2 > 0));
    printf("(num1 > 0 || num2 > 0) : %d\n", (num1 > 0 || num2 > 0));
    printf("!(num1 > 0)            : %d\n", !(num1 > 0));

    return 0;
}
