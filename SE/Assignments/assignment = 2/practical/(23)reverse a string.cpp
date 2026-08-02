#include <stdio.h>
#include <string.h>

int main()
{
    char str[100], rev[100];
    int i, len, flag = 0;

    printf("Enter a string: ");
    gets(str);

    len = strlen(str);

    // Reverse the string
    for(i = 0; i < len; i++)
    {
        rev[i] = str[len - i - 1];
    }
    rev[i] = '\0';

    printf("Reversed string: %s\n", rev);

    // Check palindrome
    for(i = 0; i < len; i++)
    {
        if(str[i] != rev[i])
        {
            flag = 1;
            break;
        }
    }

    if(flag == 0)
        printf("The string is Palindrome");
    else
        printf("The string is Not Palindrome");

    return 0;
}
