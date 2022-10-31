// Kata url: https://www.codewars.com/kata/55da6c52a94744b379000036.

int eat_string_digit(char **string)
{
    int i = 0;
    char *str = *string;

    while (*str && *str >= '0' && *str <= '9')
    {
        i *= 10;
        i += *str - '0';
        str++;
    }

    *string = str;
    return i;
}

unsigned sum_string_integers(char *string)
{
    int total = 0;

    while (*string) {
        if (*string >= '0' && *string <= '9') {
            int x = eat_string_digit(&string);
            total += x;
        } else {
            string++;
        }
    }
    return total;
}
