class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        resCount = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # there is overlapping
            if prevEnd > start:
                resCount += 1
                # skip the interval whose end time is later
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return resCount