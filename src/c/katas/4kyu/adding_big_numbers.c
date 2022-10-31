#include <stdlib.h>
#include <stdio.h>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

int get_strlen(const char *str)
{
    const char *ptr = str;

    while (*str++);
    return str - ptr;
}

char *get_padded_string(const char *str, int to_pad)
{
    char *out = malloc(sizeof(char) * (get_strlen(str) + to_pad + 1));
    char *ptr = out;

    for (; to_pad > 0; to_pad--)
        *(ptr++) = '0';
    while (*str)
        *(ptr++) = *(str++);
    *(ptr++) = '\0';
    return out;
}

char *handle_last_ret(char *current, int len)
{
    char *out = malloc(sizeof(char) * (len + 1));
    out[0] = '1';
    for (int i = 0; i < len; i++) {
        out[i + 1] = current[i];
    }
    free(current);
    return out;
}

char *add_len_eq_str(const char *a, const char *b, int len)
{
    int digit;
    int ret = 0;
    int len_cpy = len;
    char *out = malloc(sizeof(char) * len);

    while (len--) {
        digit = (a[len] - '0') + (b[len] - '0') + ret;
        ret = (digit > 9);
        out[len] = '0' + (digit - (10 * ret));
    }
    out[len_cpy - 1] = '\0';
    return (ret)? handle_last_ret(out, len_cpy): out;
}

char *add(const char *a, const char *b)
{
    int len_a = get_strlen(a);
    int len_b = get_strlen(b);
    int diff = len_b - len_a;

    if (diff > 0) {
        a = get_padded_string(a, diff);
        len_a = len_b;
    } else if (diff < 0) {
        b = get_padded_string(b, -diff);
    }
    return add_len_eq_str(a, b, len_a);
}
