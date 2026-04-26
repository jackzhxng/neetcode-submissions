"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x : x.start)
        prev = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start < prev.end:
                return False
            prev = interval
        return True