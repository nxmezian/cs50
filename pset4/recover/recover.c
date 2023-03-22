#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef uint8_t BYTE;

BYTE buffer[512];

int BLOCK_SIZE =  512;

int main(int argc, char *argv[])
{
    //checks if exactly one cmd-line argument is used
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //opens and reads file
    FILE *file = fopen(argv[1], "r");

    //if file cannot be read, returns exit code 2
    if (file == NULL)
    {
        printf("File cannot be opened");
        return 2;
    }

    //creates pointer for files to be written
    FILE *restored_file = NULL;
    char *file_name = malloc(8 * sizeof(buffer));

    //keeps track of the number of images
    int image_count = 0;


    //reads into the given file
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        //checks if the file is a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff
            && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(file_name, "%03i.jpg", image_count);
            restored_file = fopen(file_name, "w");
            image_count += 1;
        }
        if (restored_file != NULL)
        {
            //restores the photos
            fwrite(buffer, 1, BLOCK_SIZE, restored_file);
        }
    }
    free(file_name);
}