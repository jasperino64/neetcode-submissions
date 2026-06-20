class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visit = set()
        
        for course, pre in prerequisites:
            preMap[course].append(pre)        

        def hasCycle(i):
            if not preMap[i]:
                return False

            if i in visit:
                return True
            
            visit.add(i)
            for pre in preMap[i]:
                if hasCycle(pre):
                    print(pre)
                    return True
            
            visit.remove(i)
            preMap[i] = []
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True
