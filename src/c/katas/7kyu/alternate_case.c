char *alternateCase (char *string)
{
    char c;
    for (int i = 0; (c = string[i]); i++)
    {
        if (c >= 'A' && c <= 'Z') {
            string[i] += 32;
            continue;
        }
      
        if (c >= 'a' && c <= 'z') {
            string[i] -= 32;
            continue;
        }
    }

    return string;
}
