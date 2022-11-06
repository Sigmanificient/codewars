// Kata url: https://www.codewars.com/kata/546dba39fa8da224e8000467.
#include <stddef.h>
#include <stdlib.h>

typedef struct char_info {
	unsigned count;
	unsigned char value;
} char_info_t;

int get_diff_char_count(const char *str)
{
    int count = 1;
    char prev = *str;

    if (prev == '\0') {
        return 0;
    }
    while (*str) {
        if (prev != *str) {
            prev = *str;
            count++;
        }
        str++;
    }
    return count;
}

char_info_t *run_length_encoding(const char *str, size_t *length_out)
{
    int count_out = get_diff_char_count(str);
    char_info_t *out = malloc(sizeof (char_info_t) * count_out);
    char prev = '\0';
    int i = -1;

    while (*str) {
        if (*str != prev) {
            out[++i] = (char_info_t) {0, *str};
            prev = *str;
        }
        str++;
        out[i].count++;
    }
    *length_out = count_out;
    return out;
}
