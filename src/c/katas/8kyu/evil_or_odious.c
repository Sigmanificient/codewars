const char *evil(int value) {
    int count = 0;

    while (value) {
        if (value & 1)
            count++;
        value >>= 1;
    }
    return (count & 1) ? "It's Odious!": "It's Evil!";
}