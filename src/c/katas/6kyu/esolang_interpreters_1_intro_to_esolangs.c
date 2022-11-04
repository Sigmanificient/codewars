// Kata url: https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0.
#include <stdlib.h>

char *alloc_output_string(const char *code)
{
    int dots = 0;

    while (*code) {
        if (*code == '.') {
            dots++;
        }
        code++;
    }
    return malloc(sizeof(char) * (dots + 1));
}

char *my_first_interpreter (const char *code)
{
    unsigned char cell = 0;
    int dot = 0;
    char *out = alloc_output_string(code);

    if (out == NULL)
        return NULL;
    while (*code) {
        if (*code == '.') {
            out[dot] = cell;
            dot++;
        }
        if (*code == '+') {
            cell++;
        }
        code++;
    }
    out[++dot] = '\0';
    return out;
}
