// https://www.codewars.com/kata/568dc69683322417eb00002c.
#include <stdbool.h>

bool triple_x(const char *s)
{
    while (*s && *s != 'x')
        s++;
    if (!*s || !*++s)
        return false;
    return *s == s[1] && *s == 'x';
}
