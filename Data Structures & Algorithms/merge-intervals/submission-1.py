class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start, end in intervals:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1] = [ans[-1][0], max(end, ans[-1][1])]
        return ans