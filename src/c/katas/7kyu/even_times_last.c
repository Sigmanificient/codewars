// Kata url: https://www.codewars.com/kata/5a1a9e5032b8b98477000004.
#include <stddef.h>

int even_last(const int array[], size_t z) {
    int sum = 0;

    for (size_t i = 0; i < z; i += 2) {
        sum += array[i];
    }
    return sum * array[z - 1];
}
