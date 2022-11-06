// Kata url: https://www.codewars.com/kata/5831c204a31721e2ae000294.

char *capitalize_vowels(char *string)
{
    char *ptr = string;
    char c;

    while ((c = *string)) {
        c &= '_';
        if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            *string = c;
        }
        string++;
    }

    return ptr;
}