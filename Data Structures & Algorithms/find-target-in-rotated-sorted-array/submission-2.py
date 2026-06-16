class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]: l = m + 1
            else: r = m 
        pivot = l
        def binarysearch(left, right):
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target: return mid
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
            return -1
        
        return max(binarysearch(pivot, len(nums) - 1), binarysearch(0, pivot - 1))