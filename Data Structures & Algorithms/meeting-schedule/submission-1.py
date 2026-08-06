"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        listOfMeetings = []
        for interval in intervals:
            listOfMeetings.append([interval.start, interval.end])
        listOfMeetings.sort(key=lambda x: x[0])

        for idx in range(1, len(listOfMeetings)):
            if listOfMeetings[idx-1][1] > listOfMeetings[idx][0]:
                return False
        return True
