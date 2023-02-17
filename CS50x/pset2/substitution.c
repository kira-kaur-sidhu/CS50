// Substitution - Design and implement a program, substitution, that encrypts messages using a substitution cipher.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void substitute_text(string text, string key);

int main(int argc, string argv[])
{
    // Check if arg is missing or too many
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check key length
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Check for non-alpha letters
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isalpha(argv[1][i]))
        {
            // Check for duplicate letters
            for (int k = i + 1; k < strlen(argv[1]); k++)
            {
                if (argv[1][i] == argv[1][k])
                {
                    printf("Key must not contain duplicate letters.\n");
                    return 1;
                }
            }
        }

        else
        {
            printf("Key must contain only alphabetic characters.\n");
            return 1;
        }
    }

    // Get input and output ciphered text
    string text = get_string("plaintext: ");
    printf("ciphertext: ");
    substitute_text(text, argv[1]);
    return 0;

}

void substitute_text(string text, string key)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if isupper(text[i])
        {
            int position = text[i] - 65;
            char ch = key[position];
            printf("%c", toupper(ch));
        }
        else if islower(text[i])
        {
            int position = text[i] - 97;
            char ch = key[position];
            printf("%c", tolower(ch));
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}
