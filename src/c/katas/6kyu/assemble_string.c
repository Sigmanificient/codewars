/* Kata url: https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6 */
#include <string.h>

char *assemble_string(char *assembled, size_t rows, const char *const strings[rows])
{
    size_t len = rows ? strlen(*strings) : 0;

    assembled[len] = '\0';
    memset(assembled, '#', len);

    for (size_t i = 0; i < len; i++)
        for (size_t y = 0; y < rows; y++)
            if (strings[y][i] != '*')
                assembled[i] = strings[y][i];

    return assembled;
}
