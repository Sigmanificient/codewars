#include <stddef.h>

char *nth_char(size_t length, const char *const strings[length], char *str_out)
{
    for (size_t i = 0; i < length; i++) {
        str_out[i] = strings[i][i];
    }
    str_out[length] = '\0';
    return str_out;
}
