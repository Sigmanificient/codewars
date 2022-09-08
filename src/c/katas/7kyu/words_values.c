#include <stddef.h>

const int* name_value(size_t n, const char* const words[n])
{
    int* vals = (int*)malloc(n * sizeof(int));
    int total;
    int j;
    char c;

    for (size_t i = 0; i < n; i++)
    {
        total = 0;
        j = 0;

        while ((c = words[i][j++]) != '\0')
        {
            if (c == ' ') continue;
            total += (c - 'a') + 1;
        }

        vals[i] = total * (i + 1);
    }

    return vals;
}
