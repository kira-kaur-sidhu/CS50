#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get and print name
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
