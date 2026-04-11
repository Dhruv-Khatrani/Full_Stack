#include <stdio.h>

int main()
{
    int choice, qty;
    float total = 0;
    char more;

    do
    {
        // Display Food Menu
        printf("\n------ FOOD MENU ------\n");
        printf("1. Pizza      - 200 Rs\n");
        printf("2. Burger     - 100 Rs\n");
        printf("3. Sandwich   - 80 Rs\n");
        printf("4. Cold Drink - 50 Rs\n");
        printf("5. Pasta      - 150 Rs\n");

        // Take user choice
        printf("Enter item number: ");
        scanf("%d", &choice);

        printf("Enter quantity: ");
        scanf("%d", &qty);

        // Conditional statements for billing
        if(choice == 1)
        {
            total = total + (200 * qty);
        }
        else if(choice == 2)
        {
            total = total + (100 * qty);
        }
        else if(choice == 3)
        {
            total = total + (80 * qty);
        }
        else if(choice == 4)
        {
            total = total + (50 * qty);
        }
        else if(choice == 5)
        {
            total = total + (150 * qty);
        }
        else
        {
            printf("Invalid choice!\n");
        }

        // Ask user if they want to order more
        printf("Do you want to order more items? (y/n): ");
        scanf(" %c", &more);

    } while(more == 'y' || more == 'Y'); 

    // Display final bill
    printf("\n------ FINAL BILL ------\n");
    printf("Total Amount = Rs %.2f\n", total);

    return 0;
}
