// Kata url: https://www.codewars.com/kata/5a58d889880385c2f40000aa.

int ten_power(int n)
{
    int count = 1;

    while (n) {
        n /= 10;
        count *= 10;
    }
    return count;
}

const char *autoMorphic(int number)
{
    int r = (number * number) % ten_power(number);
    return (r == number)? "Automorphic": "Not!!";
}
