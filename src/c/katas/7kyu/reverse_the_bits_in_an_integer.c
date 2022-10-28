// Kata url: https://www.codewars.com/kata/5959ec605595565f5c00002b

unsigned reverse_bits(unsigned n)
{
    unsigned result = 0;

    while (n) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    return result;
}
