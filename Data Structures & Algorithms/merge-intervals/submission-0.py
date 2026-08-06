class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            i += 1
            if not merged or s > merged[-1][1]: 
                merged.append([s, e])
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], e)]
            
        return merged