class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        startPoints = set([i for i in range(numCourses)])
        prereqs = {}
        needs = {}
        for end, start in prerequisites:
            needs[end] = needs.get(end, 0) + 1
            if start in prereqs: prereqs[start].append(end)
            else: prereqs[start] = [end]
            if end in startPoints: startPoints.remove(end)
        visited = set()
        queue = deque(startPoints)
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            if curr not in prereqs: continue
            for course in prereqs[curr]:
                needs[course] = needs.get(course, 0) - 1
                if needs[course] <= 0 and course not in visited:
                    queue.append(course)
        return len(visited) == numCourses