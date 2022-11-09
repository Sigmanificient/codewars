// Kata url: https://www.codewars.com/kata/586566b773bd9cbe2b000013.

int count_occ(const char *string, char delimiter)
{
    int count = 0;

    for (int i = 0; string[i]; i++) {
        if (string[i] == delimiter) {
            count++;
        }
    }
    return count;
}

char no_repeat(const char *string)
{
    for (int i = 0; string[i]; i++) {
        if (count_occ(string, string[i]) == 1) {
            return string[i];
        }
    }
    return '\0';
}
