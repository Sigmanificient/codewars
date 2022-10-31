//  Kata url: https://www.codewars.com/kata/580751a40b5a777a200000a1.

char *vowel_one(const char *input, char *output)
{
    int i = 0;
    char c;

    for (; input[i]; i++) {
        c = input[i] | ' ';
        output[i] = '0' | (
            c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
        );
    }
    output[i] = '\0';
    return output;
}
