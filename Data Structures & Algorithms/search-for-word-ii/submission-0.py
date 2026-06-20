class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        
        root = TrieNode()

        for word in words:
            root.add(word)

        res, path = set(), set()    
        def dfs(r, c, node, word):
            if node.end:
                res.add(word)
            if (r,c) in path or r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in node.children:
                return
            char = board[r][c]
            node = node.children[char]
            path.add((r,c))
            
            dfs(r + 1, c, node, word + char)
            dfs(r - 1, c, node, word + char)
            dfs(r, c + 1, node, word + char)
            dfs(r, c - 1, node, word + char)

            path.remove((r,c))
        

        
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)