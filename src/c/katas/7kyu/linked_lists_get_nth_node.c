// https://www.codewars.com/kata/55befc42bfe4d13ab1000007.
#include <stddef.h>

typedef struct List {
    struct List *next;
    int data;
} list_t;

const list_t *get_nth_node (const list_t *list, size_t n)
{
    while (list && n--) {
        list = list->next;
    }
    return list;
}
