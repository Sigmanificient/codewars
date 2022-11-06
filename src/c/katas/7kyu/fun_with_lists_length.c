// Kata url: https://www.codewars.com/kata/581e476d5f59408553000a4b.
#define NULL (0)

typedef struct node_t {
    void *data;
    struct node_t *next;
} Node;

int length(const Node *head)
{
    int length = 0;

    while (head != NULL) {
        head = head->next;
        length++;
    }
    return length;
}
