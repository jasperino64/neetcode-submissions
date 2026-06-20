class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visit = set()
        def hasCycle(x, prev):
            if x in visit:
                return True
            visit.add(x)
            for y in graph[x]:
                if y == prev:
                    continue
                if hasCycle(y,x):
                    return True
            return False
        
        if hasCycle(0, -1):
            return False
        return n == len(visit)