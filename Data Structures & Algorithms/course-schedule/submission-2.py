class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visit = set()
        for course, pre in prerequisites:
            preMap[course].append(pre)        

        def hasCycle(i):
            if i in visit:
                return True
            if i not in preMap:
                return False
            visit.add(i)
            for pre in preMap[i]:
                if hasCycle(pre):
                    print(pre)
                    return True
            visit.remove(i)
            return False

        for i in range(numCourses):
            if hasCycle(i):
                print(i)
                return False
        return True
