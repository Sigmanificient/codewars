// kata url: https://www.codewars.com/kata/5d6f49d85e45290016bf4718.
int any_odd(unsigned x) {
    return (x & 0xaaaaaaaa) != 0;
}
