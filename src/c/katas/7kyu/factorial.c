unsigned __int128 factorial(unsigned n)
{
    unsigned __int128 result = 1;

    for (unsigned i = 1; i <= n; i++)
        result *= i;

    return result;
}
