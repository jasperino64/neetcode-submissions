class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                sq =  (r//3, c//3)
                if num in cols[c] or \
                    num in rows[r] or \
                    num in squares[sq]:
                    return False
                cols[c].add(num)
                rows[r].add(num)
                squares[sq].add(num)
        
        return True