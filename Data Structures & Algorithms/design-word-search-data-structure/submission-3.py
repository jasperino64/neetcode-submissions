class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i,curr):
            if i == len(word) and curr.end:
                return True
            for i in range(i, len(word)):
                
                if word[i] == ".":
                    for node in curr.children.values():
                        if dfs(i+1, node):
                            return True
                print(i, curr)
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
            return curr.end
            

        return dfs(0,self.root)
        
