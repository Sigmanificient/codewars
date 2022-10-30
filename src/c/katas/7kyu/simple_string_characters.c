// Kata url: https://www.codewars.com/kata/5a29a0898f27f2d9c9000058.

void count_char_types(const char *string, unsigned counts[4])
{
    for (int i = 0; i < 4; i++)
        counts[i] = 0;
    for (int i = 0; string[i]; i++) {
        if (string[i] >= 'A' && string[i]<= 'Z') {
            counts[0]++;
            continue;
        }
        if (string[i] >= 'a' && string[i] <= 'z') {
            counts[1]++;
            continue;
        }
        if (string[i] >= '0' && string[i] <= '9') {
            counts[2]++;
            continue;
        }
        counts[3]++;
    }
}
