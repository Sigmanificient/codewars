// Kata url: https://www.codewars.com/kata/576bb3c4b1abc497ec000065.
#include <stdbool.h>

#define NULL (0)
#define IS_LETTER(x) ((x >= 'A' && x <= 'Z'))

int c_sum(const char *string)
{
    char c;
    int sum = 0;

    if (string == NULL)
        return 0;
    while (*string) {
        c = (*string++) & '_';
        if (!IS_LETTER(c))
            return 0;
        sum += c;
    }
    return sum;
}

bool compare(const char *s1, const char *s2) {
    return c_sum(s1) == c_sum(s2);
}
