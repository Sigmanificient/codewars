#include <stdlib.h>

size_t get_strlen(const char *str)
{
    size_t len = 0;

    while (str[len]) {
        len++;
    }
    return len;
}

char *capitalize(const char *str_in, size_t z, size_t indices[z]) {
    size_t idx;
    size_t len = get_strlen(str_in);
    char *out = malloc(len + 1);

    for (size_t i = 0; i < len; i++) {
        out[i] = str_in[i];
    }

    for (size_t i = 0; i < z; i++) {
        idx = indices[i];
        if (idx >= len) {
            continue;
        }
        out[idx] &= '_';
    }
    out[len] = '\0';
    return out;
}