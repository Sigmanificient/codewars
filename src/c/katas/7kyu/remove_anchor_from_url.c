#include <stdlib.h>

char* remove_url_anchor(const char* url_in) {
    char c;
    int n = 0;

    while ((c = url_in[n]) != '#' && c != '\0')
      n++;

    char* url_out = (char *)malloc((n + 1) * sizeof(char));

    for (int i = 0; i < n; i++)
      url_out[i] = url_in[i];

    url_out[n++] = '\0';
    return url_out;
}
