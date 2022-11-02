// Kata url: https://www.codewars.com/kata/5583d268479559400d000064.
#include <stdlib.h>

int get_strlen(const char *str)
{
    int len = 0;

    while (str[len]) {
        len++;
    }
    return len;
}

char *binary_to_string(const char *binary) {
    int length = get_strlen(binary);
    int chars_count = length / 8;
    char *out = malloc(sizeof(char) * (chars_count + 1));
    int i = 0;

    while (*binary) {
        out[i] = 0;

        for (int j = 0; j < 7; j++) {
            out[i] <<= 1;
            out[i] |= (*++binary - '0');
        }
        binary++;
        i++;
    }
    out[chars_count] = '\0';
    return out;
}
