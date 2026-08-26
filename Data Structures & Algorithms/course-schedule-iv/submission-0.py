from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])
        

        resList = []
        for query in queries:
            u, v = query[0], query[1]

            stack = deque()
            seen = set()
            resBool = False
            stack.append(u)
            seen.add(u)

            while stack:
                curr = stack.popleft()

                for nei in adj[curr]:
                    if nei == v:
                        resBool = True
                        break
                    elif nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
            resList.append(resBool)

        return resList