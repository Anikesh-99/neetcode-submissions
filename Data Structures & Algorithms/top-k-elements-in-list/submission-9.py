class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        n = len(nums)
        revCount = [[] for _ in range(n + 1)]
        for key in count:
            revCount[count[key]].append(key)
        for c in range(n, 0, -1):
            if k - len(revCount[c]) >= 0:
                ans.extend(revCount[c])
                k -= len(revCount[c])
            else:
                ans.extend(revCount[c][:k])
                break
        return ans                
