class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        targetS, targetE = newInterval
        l, r = 0, len(intervals) - 1
        mid = l + (r - l)//2
        while l <= r:
            mid = l + (r - l)//2
            s, e = intervals[mid]
            if s == targetS: break
            if s >= targetS:
                r = mid - 1
            else:
                l = mid + 1
        if intervals[mid][0] < targetS:
            intervals = intervals[:mid + 1] + [newInterval] + intervals[mid + 1:]
        else:
            intervals = intervals[:mid] + [newInterval] + intervals[mid:]
        # print(intervals)
        merged = []
        for s, e in intervals:
            if merged and merged[-1][1] >= s:
                merged[-1][1] = max(e, merged[-1][1])
            else:
                merged.append([s, e])
            # print(merged)
        return merged