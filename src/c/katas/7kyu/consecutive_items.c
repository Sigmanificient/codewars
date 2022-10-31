// Kata url: https://www.codewars.com/kata/5f6d533e1475f30001e47514.
#include <stdbool.h>
#include <stddef.h>

bool consecutive(const int *arr, size_t n, int a, int b) {
    int p = 0;
    size_t i = 0;

    for (; i < n; i++) {
        if (arr[i] == a || arr[i] == b) {
            p = (arr[i] == a) ? b: a;
            break;
        }
    }
    return (arr[i + 1] == p);
}
