#include <stdio.h>

int main() {
    int choice;
    float years, days;

    printf("Conversion Program\n");
    printf("1. Convert Years to Days\n");
    printf("2. Convert Days to Years\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &choice);

    if(choice == 1) {
        printf("Enter number of years: ");
        scanf("%f", &years);

        days = years * 365;
        printf("Days = %.2f\n", days);
    }
    else if(choice == 2) {
        printf("Enter number of days: ");
        scanf("%f", &days);

        years = days / 365;
        printf("Years = %.2f\n", years);
    }
    else {
        printf("Invalid choice!\n");
    }

    return 0;
}
