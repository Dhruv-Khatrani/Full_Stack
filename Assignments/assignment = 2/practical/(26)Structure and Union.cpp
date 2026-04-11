#include <stdio.h>
#include <string.h>

struct student
{
    int id;
    float marks;
    char grade;
};

union data
{
    int id;
    float marks;
    char grade;
};

int main()
{
    struct student s;
    union data u;

    s.id = 101;
    s.marks = 85.5;
    s.grade = 'A';

    u.id = 101;
    u.marks = 85.5;
    u.grade = 'A';

    printf("Structure Values:\n");
    printf("ID = %d\n", s.id);
    printf("Marks = %.2f\n", s.marks);
    printf("Grade = %c\n", s.grade);

    printf("\nUnion Values:\n");
    printf("ID = %d\n", u.id);
    printf("Marks = %.2f\n", u.marks);
    printf("Grade = %c\n", u.grade);

    return 0;
}
