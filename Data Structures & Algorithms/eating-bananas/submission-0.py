class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            hrs = 0
            for i in range(len(piles)):
                hrs += math.ceil(piles[i]/k)
            return hrs
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = l + (r - l)//2
            hrs = hours(m)
            if hrs <= h: ans = min(ans, m)
            if hrs > h:
                l = m + 1
            else:
                r = m - 1
        return ans