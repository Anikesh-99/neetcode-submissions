class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = []
        for s, e in intervals:
            if merged and merged[-1][1] >= s:
                merged[-1][1] = max(e, merged[-1][1])
            else:
                merged.append([s, e])
            # print(merged)
        return merged