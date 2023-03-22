#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{

    string x = ("HELLO");

    for (int i = 0; i < strlen(x); i++)
    {
        if isalpha(x[i])
        {
            char y = x[i] + 1;
            printf("%c", y);
        }
        else
        {
            char y = x[i];
            printf("%c", y);
        }


    }
    printf("\n");

}