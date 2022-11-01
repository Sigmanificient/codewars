// Kata url: https://www.codewars.com/kata/5d49c93d089c6e000ff8428c.
#include <stddef.h>

size_t save(size_t n, size_t sizes[n], size_t hd) {
    size_t filled = 0;

    for (size_t i = 0; i < n; i++) {
        filled += sizes[i];

        if (filled >= hd)
            return i;
    }
    return n;
}
