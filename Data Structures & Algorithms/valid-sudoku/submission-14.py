from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                sq = (r // 3, c // 3)
                val = board[r][c]
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[sq]):
                    print(val,r,c)
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[sq].add(val)

        return True
