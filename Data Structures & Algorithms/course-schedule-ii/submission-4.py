class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for i, j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)
        output = []
        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    dfs(n)
        for i in range(numCourses):
            if indegree[i] == 0: dfs(i)
        return output if len(output) == numCourses else []