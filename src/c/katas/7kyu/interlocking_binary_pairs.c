// Kata url: https://www.codewars.com/kata/628e3ee2e1daf90030239e8a.
#include <stdbool.h>

bool interlockable(unsigned long long a, unsigned long long b) {
    return !(a & b);
}
