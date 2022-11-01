// Kata url: https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca.
#include <stddef.h>

size_t catch_sign_change(const int *arr, size_t sz) {
    int count = 0;
    int sign = (*arr < 0);

    for (size_t i = 0; i < sz; i++) {
        if ((arr[i] < 0) != sign) {
            sign = !sign;
            count++;
        }
    }
    return count;
}
