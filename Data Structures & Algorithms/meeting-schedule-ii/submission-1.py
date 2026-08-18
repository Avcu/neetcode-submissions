"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        resMax = 0
        endTimes = []

        for idx in range(len(intervals)):
            currStart, currEnd = intervals[idx].start, intervals[idx].end
             
            # push the new end time to the heap
            heappush(endTimes, currEnd)

            # remove the end times that are lower than the current start time
            while endTimes and endTimes[0] <= currStart:
                heappop(endTimes)
            resMax = max(len(endTimes), resMax)
        return resMax
        