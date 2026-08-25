class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqAdj = [[] for _ in range(numCourses)]
        nextCoursesAdj = [[] for _ in range(numCourses)]
        
        for prereq in prerequisites:
            # list of required courses
            prereqAdj[prereq[0]].append(prereq[1])
            # courses becoming avaliable
            nextCoursesAdj[prereq[1]].append(prereq[0])

        stack = []
        seen = set()

        for idx in range(len(prereqAdj)):
            prereqCourses = prereqAdj[idx]
            if len(prereqCourses) == 0:
                stack.append(idx)
                seen.add(idx)
            

        while stack:
            currCourse = stack.pop()
            for nextCourse in nextCoursesAdj[currCourse]:
                prereqAdj[nextCourse].remove(currCourse)
                if len(prereqAdj[nextCourse]) == 0:
                    stack.append(nextCourse)
                    seen.add(nextCourse)
        

        return len(seen) == numCourses