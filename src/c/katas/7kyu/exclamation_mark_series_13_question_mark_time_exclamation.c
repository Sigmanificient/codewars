// Kata url: https://www.codewars.com/kata/57fb142297e0860073000064.

unsigned product(const char *string)
{
    int qm = 0;
    int em = 0;

    while (*string) {
        if (*string == '?') {
            qm++;
        }
        if (*string == '!') {
            em++;
        }
        string++;
    }
    return em * qm;
}
