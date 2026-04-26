"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Time taken: 12 mins
        """
        intervals.sort(key=lambda x: x.start)
        rooms = []
        min_rooms = 0
        for interval in intervals:
            while rooms and rooms[0] <= interval.start:
                _ = heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
            min_rooms = max(min_rooms, len(rooms))
        return min_rooms
            
        