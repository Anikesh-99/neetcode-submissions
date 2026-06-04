class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        hm = defaultdict(list)
        for key in count:
            value = count[key]
            hm[value].append(key)
        ans = []
        for c in range(len(nums), 0, -1):
            if c in hm:
                ans.extend(hm[c])
            if len(ans) > k:
                return ans[:k]
        return ans