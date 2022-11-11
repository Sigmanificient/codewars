// Kata url: https://www.codewars.com/kata/522551eee9abb932420004a0.

typedef unsigned long long ull;

ull nth_fib(int n) {
    ull a = 0;
    ull b = 1;
    ull swap;

    for (int i = 0; i < n; i++) {
        swap = b;
        b = a + b;
        a = swap;
    }
    return a;
}
