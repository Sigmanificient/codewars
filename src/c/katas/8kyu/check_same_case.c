#define abs(x) ((x)<0 ? (-x) : (x))

int is_upper(char k)
{
    return k >= 'A' && k <= 'Z';
}

int is_lower(char k)
{
    return k >= 'a' && k <= 'z';
}

int same_case(char a, char b)
{
    int c = 0;
    c += is_upper(a) - is_lower(a);
    if (!c) return -1;

    int guard = c;
    c += is_upper(b) - is_lower(b);
    if (c == guard) return -1;

    return abs(c) == 2;
}
