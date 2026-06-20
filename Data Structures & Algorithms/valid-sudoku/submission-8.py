class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                sq = (r//3, c//3)
                x = board[r][c]
                if x in rows[r] or x in cols[c] or x in squares[sq]:
                    return False
                rows[r].add(x)
                cols[c].add(x)
                squares[sq].add(x)
        return True