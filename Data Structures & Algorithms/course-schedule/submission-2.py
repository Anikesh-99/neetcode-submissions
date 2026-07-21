class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        startPoints = set([i for i in range(numCourses)])
        mapping = {}
        revMap = {}
        for x, y in prerequisites:
            if x not in mapping:
                mapping[x] = 1
                startPoints.remove(x)
            else:
                mapping[x] += 1
            if y not in revMap:
                revMap[y] = [x]
            else:
                revMap[y].append(x)
        # print(startPoints)
        if not startPoints: return False
        startPoints = list(startPoints)
        visited = set()
        while startPoints:
            curr = startPoints.pop(0)
            if curr in visited: continue
            visited.add(curr)
            dep = revMap[curr] if curr in revMap else []
            for d in dep:
                mapping[d] -= 1
                if mapping[d] == 0:
                    startPoints.append(d)
        return len(visited) == numCourses
            