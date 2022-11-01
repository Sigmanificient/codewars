// Kata url: https://www.codewars.com/kata/5a262cfb8f27f217f700000b.
#include <stdlib.h>
#include <string.h>

int char_in_str(char c, char const *str)
{
    char *ptr = (char *)str;

    while (*ptr) {
        if (*ptr == c)
            return 1;
        ptr++;
    }
    return 0;
}

char *solve(const char *a, const char *b) {
    int max_len = strlen(a) + strlen(b);
    char *tmp_out = malloc(sizeof(char) * max_len + 1);
    int idx = 0;

    for (int i = 0; a[i]; i++)
        if (!char_in_str(a[i], b))
            tmp_out[idx++] = a[i];
    for (int i = 0; b[i]; i++)
        if (!char_in_str(b[i], a))
            tmp_out[idx++] = b[i];
    tmp_out[idx] = '\0';
    return tmp_out;
}
