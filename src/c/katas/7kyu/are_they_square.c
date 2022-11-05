// Kata url: https://www.codewars.com/kata/56853c44b295170b73000007.
#include <stdbool.h>
#include <stddef.h>

bool is_n_square(int n)
{
    int j = 0;

    for (int i = 0; j < n; i++)
        j = i * i;
    return j == n;
}

bool is_square(const unsigned arr[], size_t size)
{
    if (!size)
        return false;
    for (size_t i = 0; i < size; i++)
        if (!is_n_square(arr[i]))
            return false;
    return true;
}
