// Kata url: https://www.codewars.com/kata/5a0d38c9697598b67a000041.
long eliminate_unset_bits(const char* number) {
    long count = 1;

    while (*number) {
        if (*number == '1') {
            count <<= 1;
        }
        number++;
    }
    return count - 1;
}
