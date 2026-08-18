class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resList = []
        newStart, newEnd = newInterval[0], newInterval[1]

        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newStart:
            resList.append(intervals[idx])
            idx += 1
        

        while idx < len(intervals) and newEnd >= intervals[idx][0]:
            newStart = min(newStart, intervals[idx][0])
            newEnd = max(newEnd, intervals[idx][1])
            idx += 1
        resList.append([newStart, newEnd])

        while idx < len(intervals):
            resList.append(intervals[idx])
            idx += 1
        return resList