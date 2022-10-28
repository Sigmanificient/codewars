// Kata url: https://www.codewars.com/kata/593c9175933500f33400003e.
#include <stdlib.h>

double *multiples(int m, double n) {
    double *out = malloc(sizeof(double) * m);
    double sum = n;

    for (int i = 0; i < m; i++) {
        out[i] = sum;
        sum += n;
    }
    return out;
}
