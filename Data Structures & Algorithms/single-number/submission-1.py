class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import functools
        return functools.reduce(lambda x, y: x ^ y, nums)