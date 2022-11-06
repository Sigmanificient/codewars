// Kata url: https://www.codewars.com/kata/5982619d2671576e90000017.

char *spongebob_case(const char *str_in, char *str_out)
{
    char c;
    int i = 0;

    for (; str_in[i]; i++) {
        c = str_in[i] | ' ';

        if (c < 'a' || c > 'z') {
            str_out[i] = str_in[i];
            continue;
        }
        if (i & 1) {
            str_out[i] = c;
        } else {
            str_out[i] = str_in[i] & '_';
        }
    }
    str_out[i] = '\0';
    return str_out;
}
