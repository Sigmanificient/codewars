// Kata url: https://www.codewars.com/kata/5a97387e5ee396e70a00016d.
#include <stdlib.h>

const char *pofi(unsigned n) {
    int is_i = (n & 1);
    int minus = (n % 4) > 1;
    char *out = malloc(sizeof(char) * (is_i + minus + 1));

    if (minus)
        out[0] = '-';
    out[minus] = (is_i)? 'i': '1';
    out[minus + 1] = '\0';
    return out;
}
