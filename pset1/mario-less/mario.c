//creates a pyramid-like structure with a height based on the user's input
#include <cs50.h>
#include <stdio.h>

int main(void)
{

//input of "height" sets the exact height for the pyramid with a a minimum of 1 and a max of 8

    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

//prints a pyramid consisting of spaces and hashes (#)
    for (int i = 0; i < height; i++)
    {
        for (int j = i; j < height - 1; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }


}