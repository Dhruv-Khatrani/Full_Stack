//1. Monday to Sunday using switch case

#include <stdio.h>

int main() {
    int day;

    printf("Enter number (1-7): ");
    scanf("%d", &day);

    switch(day) {
        case 1:
            printf("Monday");
            break;
        case 2:
            printf("Tuesday");
            break;
        case 3:
            printf("Wednesday");
            break;
        case 4:
            printf("Thursday");
            break;
        case 5:
            printf("Friday");
            break;
        case 6:
            printf("Saturday");
            break;
        case 7:
            printf("Sunday");
            break;
        default:
            printf("Invalid input! Enter number between 1 and 7.");
    }

    return 0;
}

//2. Vowel or Consonant using switch case

#include <stdio.h>

int main() {
    char ch;

    printf("Enter a character: ");
    scanf(" %c", &ch); 

    switch(ch) {
        case 'a': case 'A':
        case 'e': case 'E':
        case 'i': case 'I':
        case 'o': case 'O':
        case 'u': case 'U':
            printf("%c is a Vowel\n", ch);
            break;
        default:
            printf("%c is a Consonant\n", ch);
    }

    return 0;
}  

