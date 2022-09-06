char* make_acronym (const char *words, char *letters)
{
    char c;
    int i = 0;
    int idx = 0;

    letters[idx++] = words[i++];

    while ((c = words[i]) != '\0') {
        if (words[i - 1] == ' ') {
            letters[idx] = c;
            idx++;
        }

        i++;
    }

    letters[idx++] = '\0';
    return letters;
}
