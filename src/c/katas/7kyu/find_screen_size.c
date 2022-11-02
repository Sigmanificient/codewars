#include <stdlib.h>

int parse_int(char **str, char end_char)
{
    int n = 0;

    while (**str != end_char) {
        n *= 10;
        n += *(*str) - '0';
        (*str)++;
    }
    (*str)++;
    return n;
}

int get_dn(int n)
{
    int d = 0;

    while (n) {
        n /= 10;
        d++;
    }
    return d;
}

char *write_int_to_str(char *in, int n, int *size)
{
    while (n != 0) {
        in[*size] = '0' + (n % 10);
        n /= 10;
        (*size)--;
    }
    return in;
}

char *write_str(int height, int width, int str_size)
{
    char *out = malloc(sizeof(char) * (str_size + 1));

    out[--str_size] = '\0';
    out = write_int_to_str(out, height, &str_size);
    out[str_size--] = 'x';
    out = write_int_to_str(out, width, &str_size);
    return out;
}


char *find_screen_height(int width, char *ratio)
{
    int left = parse_int(&ratio, ':');
    int right = parse_int(&ratio, '\0');
    int height = (width * right) / left;

    return write_str(height, width, (get_dn(height) + get_dn(width) + 1));
}
