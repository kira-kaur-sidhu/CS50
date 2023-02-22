// Recover - write a program that iterates over a copy of my memory card, looking for JPEGs’ signatures. Each time you find a signature, you can open a new file for writing and start filling that file with bytes from my memory card, closing that file only once you encounter another signature

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if only 1 command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    // Check if file exists
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Assign values and variables
    typedef uint8_t BYTE;

    BYTE buffer[512];
    char *filename = malloc(8);

    int BLOCK_SIZE = 512 * sizeof(uint8_t);
    int count = 0;

    FILE *img = NULL;

    // Read over file and write into new image file
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count != 0)
                fclose(img);

            sprintf(filename, "%03i.jpg", count);
            count++;
            img = fopen(filename, "w");
        }

        if (img != NULL)
            fwrite(buffer, BLOCK_SIZE, 1, img);
    }

    free(filename);
    fclose(img);
    fclose(file);
    return 0;
}
