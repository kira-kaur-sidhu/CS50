// Readability - Design and implement a program, readability, that computes the Coleman-Liau index of text.

#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Get User Input
    string text = get_string("Text: ");

    // Count number of letters in input
    int letters = count_letters(text);
    printf("%i letters\n", letters);

    // Count number of words in input
    int words = count_words(text);
    printf("%i words\n", words);

    // Count number of sentences in input
    int sentences = count_sentences(text);
    printf("%i sentences\n", sentences);

    // Return grade level with the Coleman-Liau index
    // index = 0.0588 * L - 0.296 * S - 15.8
    float L = (float) letters / words;
    float S = (float) sentences / words;

    float index = 0.0588 * (L * 100) - 0.296 * (S * 100) - 15.8;

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string text)
// Count number of letters in input
{
    int count = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            count += 1;
        }
    }
    return count;
}

int count_words(string text)
// Count number of words in input seperated by a space or dash
{
    int count = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 32)
        {
            count += 1;
        }
    }
    return count + 1;
}

int count_sentences(string text)
{
    int count = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            count += 1;
        }
    }
    return count;
}
