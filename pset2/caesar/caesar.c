#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//get key
int main(int argc, string argv[])
{

    //evaluates command line arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    //get plaintext
    string plaintext = get_string("plaintext:  ");

    //encipher
    printf("ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isalpha(plaintext[i]))
        {
            char cipher_text = plaintext[i] + key;
            printf("%c", cipher_text);
        }
        if (!isalpha(plaintext[i]))
        else
        {
            char cipher_text = plaintext[i];
            printf("%c", cipher_text);
        }

    }
    printf("\n");
}