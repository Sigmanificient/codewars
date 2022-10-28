#include <stdbool.h>

bool valid_spacing(const char *str_in) {
    bool is_space = 0;

    if (str_in[0] == ' ')
        return 0;
    for (int i = 0; str_in[i] != '\0'; i++) {
        if (str_in[i] != ' ') {
            is_space = 0;
            continue;
        }
        if (is_space)
            return 0;
        is_space = 1;
    }
    return !is_space;
}
