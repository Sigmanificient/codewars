// Kata url: https://www.codewars.com/kata/56b8903933dbe5831e000c76.

char *spoonerize(const char *words, char *spoonerized)
{
    int i = 1;
    int marker = 0;

    while (words[i]) {
        spoonerized[i] = words[i];
        if (spoonerized[i] == ' ') {
            marker = i;
        }
        i++;
    }
    spoonerized[0] = spoonerized[marker + 1];
    spoonerized[marker + 1] = words[0];
    spoonerized[i] = '\0';
    return spoonerized;
}
