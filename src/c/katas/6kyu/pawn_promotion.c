/* Kata url: https://www.codewars.com/kata/62652939385ccf0030cb537a */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

enum Promotion { NOT_POSSIBLE, QUEEN_BISHOP, QUEEN_ROOK, KNIGHT };

const long kingMask = 0x0303030303030303;
const long pawnMask = 0x1010101010101010;

enum Promotion choose_promotion(const char chessboard[8][8])
{
    long *lines = (long *)&chessboard[0][0];
    long pawn = lines[sizeof *chessboard - 1] & pawnMask;
    long king;

    char king_col = 0, king_row = 0, pawn_col = 0;

    if (pawn == 0L)
      return NOT_POSSIBLE;
    for (; pawn; pawn >>= 8)
      pawn_col++;
  
    for (size_t i = 0; i < sizeof *chessboard; i++) {
      king = lines[i] & kingMask;
      if (king) {
        king_row = i;
        break;
      }
    }
    if (!king)
      return NOT_POSSIBLE;
    for (; king; king >>= 8)
      king_col++;

    if (king_row == (sizeof *chessboard - 1) || king_col == pawn_col)
      return QUEEN_ROOK;

    char diff_x = abs(king_col - pawn_col);
    char diff_y = abs((sizeof *chessboard - 1) - king_row);

    if (diff_y == diff_x)
      return QUEEN_BISHOP;
    if ((diff_x == 2 && diff_y == 1) || (diff_x == 1 && diff_y == 2))
      return KNIGHT;
    return NOT_POSSIBLE;
}