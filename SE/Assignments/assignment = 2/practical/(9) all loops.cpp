/*
1. WAP to print 972 to 897 using for loop
2. WAP to take 10 no. Input from user and find out …
3. How many Even numbers are there
4. How many odd numbers are there
5. Sum of even numbers
6. Sum of odd numbers 
WAP to print table up to given numbers 

*/
// (1)
#include <stdio.h>

int main() {
    int i;

    for(i = 972; i >= 897; i--) {
        printf("%d\n", i);
    }

    return 0;
}

// (2-6)

#include <stdio.h>

int main() {
    int i, num;
    int evenCount = 0, oddCount = 0;
    int evenSum = 0, oddSum = 0;

    for(i = 1; i <= 10; i++) {
        printf("Enter number %d: ", i);
        scanf("%d", &num);

        if(num % 2 == 0) {
            evenCount++;
            evenSum += num;
        } else {
            oddCount++;
            oddSum += num;
        }
    }

    printf("\nTotal Even Numbers = %d", evenCount);
    printf("\nTotal Odd Numbers = %d", oddCount);
    printf("\nSum of Even Numbers = %d", evenSum);
    printf("\nSum of Odd Numbers = %d", oddSum);

    return 0;
}

// WAP to print table up to given numbers 

#include <stdio.h>

int main() {
    int num, i;

    printf("Enter a number: ");
    scanf("%d", &num);

    for(i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
    }

    return 0;
}

