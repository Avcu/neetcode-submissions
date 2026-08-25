class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numberOfPrereq = [0 for _ in range(numCourses)]
        prereqAdj = [[] for _ in range(numCourses)]
        
        for prereqs in prerequisites:
            course, pre = prereqs[0], prereqs[1]
            # number of required courses
            numberOfPrereq[course] += 1
            # list of next courses that require this course
            prereqAdj[pre].append(course)

        stack = []
        seen = set()

        for idx in range(len(numberOfPrereq)):
            if numberOfPrereq[idx] == 0:
                stack.append(idx)
                seen.add(idx)
            

        while stack:
            currCourse = stack.pop()
            for nextCourse in prereqAdj[currCourse]:
                numberOfPrereq[nextCourse] -= 1
                if numberOfPrereq[nextCourse] == 0:
                    stack.append(nextCourse)
                    seen.add(nextCourse)
        

        return len(seen) == numCourses