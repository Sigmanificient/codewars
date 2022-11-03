// Kata url: https://www.codewars.com/kata/59f7fc109f0e86d705000043.
#include <stdbool.h>

bool divisible_by_three(const char* strin) {
    int d = 0;

    for (int i = 0; strin[i]; i++) {
        d += (strin[i] - '0');
    }
    return !(d % 3);
}
