"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        queue, ans = [], 0
        for interval in intervals:
            s, e = interval.start, interval.end
            while queue and queue[0] <= s:
                heapq.heappop(queue)
            heapq.heappush(queue, interval.end)
            # print(queue)
            ans = max(len(queue), ans)
        return ans