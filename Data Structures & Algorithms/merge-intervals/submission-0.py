class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        resList = []
        newStart, newEnd = intervals[0][0], intervals[0][1]
        for start, end in intervals:
            if newEnd < start:
                resList.append([newStart, newEnd])
                newStart, newEnd = start, end
            else:
                newEnd = max(newEnd, end)
        resList.append([newStart, newEnd])
        return resList