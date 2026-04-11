#include <stdio.h>

struct employee
{
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main()
{
    struct employee e;

    printf("Enter Employee Number: ");
    scanf("%d", &e.empno);

    printf("Enter Employee Name: ");
    scanf("%s", e.empname);

    printf("Enter Address: ");
    scanf("%s", e.address);

    printf("Enter Age: ");
    scanf("%d", &e.age);

    printf("\nEmployee Details:\n");
    printf("Employee Number: %d\n", e.empno);
    printf("Employee Name: %s\n", e.empname);
    printf("Address: %s\n", e.address);
    printf("Age: %d\n", e.age);

    return 0;
}
