class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: l = m + 1
            else: r = m
        pivot = l
        def binSearch(l, r):
            while l <= r:
                m = l + (r - l)//2
                if nums[m] == target: return m
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        return max(binSearch(0, pivot - 1), binSearch(pivot, n - 1))
            