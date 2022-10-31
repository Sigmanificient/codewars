// https://www.codewars.com/kata/6071ef9cbe6ec400228d9531
struct node
{
    int value;
    struct node* left;
    struct node* right;
};


int sumTheTreeValues(struct node* root)
{
    int total = root->value;

    if (root->left)
        total += sumTheTreeValues(root->left);
    if (root->right)
        total += sumTheTreeValues(root->right);
    return total;
}