// Kata url: https://www.codewars.com/kata/5a55f04be6be383a50000187.

const char *specialNumber(int number)
{
    while (number) {
        if (number % 10 > 5) {
            return "NOT!!";
        }
        number /= 10;
    }
    return "Special!!";
}
