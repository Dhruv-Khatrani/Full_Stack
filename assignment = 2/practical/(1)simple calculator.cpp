 #include <stdio.h>

int main() {
    int num1, num2, choice;

    printf("Simple Calculator\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Modulo\n");

    printf("Enter your choice (1-5): ");
    scanf("%d", &choice);

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    switch(choice) {
        case 1:
            printf("Result = %d\n", num1 + num2);
            break;

        case 2:
            printf("Result = %d\n", num1 - num2);
            break;

        case 3:
            printf("Result = %d\n", num1 * num2);
            break;

        case 4:
            if(num2 != 0)
                printf("Result = %d\n", num1 / num2);
            else
                printf("Division by zero is not allowed.\n");
            break;

        case 5:
            if(num2 != 0)
                printf("Result = %d\n", num1 % num2);
            else
                printf("Modulo by zero is not allowed.\n");
            break;

        default:
            printf("Invalid choice\n");
    }

    return 0;
}


