class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True # has cycle
            visit[c] = False # no cycle
            res.append(c) 
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
