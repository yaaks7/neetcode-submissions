"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_ptr, end_ptr = 0,0
        rooms, max_rooms = 0,0

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        while start_ptr < len(starts):
            if starts[start_ptr]< ends[end_ptr]:
                rooms +=1
                max_rooms = max(max_rooms, rooms)
                start_ptr+=1
            else :
                rooms -=1
                end_ptr+=1
            
        return max_rooms



        