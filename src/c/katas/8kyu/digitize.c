/* Kata url: https://www.codewars.com/kata/5583090cbe83f4fd8c000051. */
#include <stddef.h>
#include <inttypes.h>

void digitize(uint64_t n, uint8_t digits[], size_t *length_out)
{
    *length_out = 0;
    do digits[(*length_out)++] = n % 10;
        while ((n /= 10));
}
