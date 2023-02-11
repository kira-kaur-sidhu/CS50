#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int size);

int main(void)
{
    // Get size of row
    int n = get_size();

    // Prints row of bricks
    print_grid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);
    return n;
}

void print_grid(int size)
{
    int spaces = size - 2;
    for (int i = 0; i < size; i++)
    {
        if (i > 0)
        {
            printf("%*s", spaces, "");
            spaces --;
            for (int k = 0; k < i; k++)
            {
                printf("%.*s", i, "#");
            }
        }
        else
        {
            printf("%*s", size - 1, "");
        }
        printf("#  #");

        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
