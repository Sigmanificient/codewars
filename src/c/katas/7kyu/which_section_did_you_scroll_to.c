#include <stdlib.h>

int get_section_id(int scroll, int *sizes, size_t sizes_length) {
    for (size_t c = 0; c < sizes_length; c++)
    {
        scroll -= sizes[c];
        if (scroll < 0)
        {
            return c;
        }
    }
    return -1;
}
