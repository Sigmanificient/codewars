// Kata url: https://www.codewars.com/kata/5983cba828b2f1fd55000114.
#include <sys/types.h>

size_t odd_one(const int *arr, size_t z) {
    for (size_t i = 0; i < z; i++) {
        if (arr[i] & 1) {
            return i;
        }
    }
    return -1;
}
