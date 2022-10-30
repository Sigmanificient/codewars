// Kata url: https://www.codewars.com/kata/5962ddfc2f9addd52200001d.
#define P_LIMIT 100000
#define HEX_CHAR_TO_INT(c) ((c & 15) + ((c > '9') ? 9: 0))

unsigned long hex_to_ul(const char *hex)
{
    unsigned long out = 0;
    while(*hex) {
        out <<= 4;
        out += HEX_CHAR_TO_INT(*hex);
        hex++;
    }
    return out;
}

int is_prime(int p)
{
    if (p == 2)
        return 1;
    if ((p & 1) == 0)
        return 0;
    for (int i = 3; i * i <= p; i += 2) {
        if (p % i == 0)
            return 0;
    }
    return 1;
}

unsigned long find_key(const char *encryption_key) {
    unsigned long key = hex_to_ul(encryption_key);
    unsigned long j;

    for (unsigned long i = 3; i < P_LIMIT; i++) {
        if (!is_prime(i))
            continue;

        j = key / i;
        if (j > P_LIMIT || (j * i) != key || !is_prime(j))
            continue;
        return (i - 1) * (j - 1);
    }
    return 0;
}
