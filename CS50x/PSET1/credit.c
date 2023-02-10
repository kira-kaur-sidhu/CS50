#include <cs50.h>
#include <stdio.h>

int checksum(long n);

int main(void)
{
    long n = get_long("Number: ");

    int check = checksum(n) % 10;
    long n_sum = n;
    int count = 0;
    do{
        n_sum = n_sum / 10;
        ++count;
    }
    while (n_sum != 0);

    if (check == 0)
    {
        long reverse_n = 0;

        while (n > 0)
        {
            reverse_n = reverse_n * 10 + n % 10;
            n = n / 10;
        }

        int x = (reverse_n / 10) % 10;
        if ((reverse_n % 10) == 3 && count == 15 && (x == 3 || x == 7))
        {
            printf("%s\n", "AMEX");
        }
        else if ((reverse_n % 10) == 4 && (count == 13 || count == 16))
        {
            printf("%s\n", "VISA");
        }
        else if ((reverse_n % 10) == 5 && count == 16 && (x == 1 || x == 2 || x == 3 || x == 4 || x == 5))
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


int checksum(long n)
{
    long n_sum = n;
    int sum_even = 0;
    int sum_odd = 0;
    int count = 0;

    do{
        n_sum = n_sum / 10;
        ++count;
    }
    while (n_sum != 0);

    for (int i = 0; i < count; i++)
    {

        long number = n % 10;

        if (i%2 == 0)
        {
            sum_odd += number;
        }
        else
        {
            int even1 = (number * 2) % 10;
            int even2 = (number * 2) / 10;

            sum_even += (even1) + (even2);
        }
        n -= number;
        n = n / 10;
    }
    int total = sum_even + sum_odd;
    return total;
}
