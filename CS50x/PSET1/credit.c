#include <cs50.h>
#include <stdio.h>

int count(long n);
int checksum(long n);

int main(void)
{
    long n = get_long("Number: ");

    int check = checksum(n) % 10;
    int counts = count(n);

    if (check == 0)
    {
        long reverse_n = 0;
        while (n > 0)
        {
            reverse_n = reverse_n * 10 + n % 10;
            n = n / 10;
        }

        int x = (reverse_n / 10) % 10;
        if ((reverse_n % 10) == 3 && counts == 15 && (x == 3 || x == 7))
        {
            printf("%s\n", "AMEX");
        }
        else if ((reverse_n % 10) == 4 && (counts == 13 || counts == 16))
        {
            printf("%s\n", "VISA");
        }
        else if ((reverse_n % 10) == 5 && counts == 16 && (x == 1 || x == 2 || x == 3 || x == 4 || x == 5))
        {
            printf("%s\n", "MASTERCARD");
        }
        else
        {
            printf("%s\n", "INVALID");
        }
    }

    else
    {
        printf("%s\n", "INVALID");
    }
}

int count(long n)
{
    int count = 0;
    do{
        n = n / 10;
        ++count;
    }
    while (n != 0);
    return count;
}

int checksum(long n)
{
    int sum_even = 0;
    int sum_odd = 0;
    int counts = count(n);

    for (int i = 0; i < counts; i++)
    {
        long number = n % 10;

        if (i%2 == 0)
        {
            sum_odd += number;
        }
        else
        {
            sum_even += ((number * 2) % 10) + ((number * 2) / 10);
        }
        n = (n -number) / 10;
    }
    return (sum_even + sum_odd);
}
