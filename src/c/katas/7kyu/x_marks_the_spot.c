// Kata url: https://www.codewars.com/kata/5777fe3f355edbf0a5000d11.
typedef struct coords {
    int row;
    int col;
} coords_t;

coords_t x_marks_the_spot(int rows, int cols, const char array[rows][cols])
{
    coords_t found_at = {-1, -1};

    for (int rid = 0; rid < rows; rid++) {
        for (int cid = 0; cid < cols; cid++) {
            if (array[rid][cid] != 'x')
                continue;
            if (found_at.row != -1) {
                return (coords_t) {-1, -1};
            }
            found_at.row = rid;
            found_at.col = cid;
        }
    }
    return found_at;
}
