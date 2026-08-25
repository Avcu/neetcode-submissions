class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numberOfPrereq = [0 for _ in range(numCourses)]
        prereqAdj = [[] for _ in range(numCourses)]


        for prereqs in prerequisites:
            course, pre = prereqs[0], prereqs[1]
            numberOfPrereq[course] += 1
            prereqAdj[pre].append(course)

        stack = []
        resList = []

        for idx in range(numCourses):
            if numberOfPrereq[idx] == 0:
                stack.append(idx)
                resList.append(idx)

        while stack:
            curCourse = stack.pop()

            for nextCourse in prereqAdj[curCourse]:
                numberOfPrereq[nextCourse] -= 1
                if numberOfPrereq[nextCourse] == 0:
                    stack.append(nextCourse)
                    resList.append(nextCourse)
                    
        return [] if len(resList) != numCourses else resList