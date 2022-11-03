// Kata url: https://www.codewars.com/kata/51c89385ee245d7ddf000001.
#include <malloc.h>

char* solution(int n)
{
    int len = 14;
    char *out = malloc(sizeof(char) * (len + 1));
    char *base = "Value is ";

    out[len] = '\0';
    while (n) {
        out[--len] = '0' + (n % 10);
        n /= 10;
    }
    while (len-- > 9)
        out[len] = '0';
    for (int i = len; i >= 0; i--)
        out[i] = base[i];
    return out;
}
