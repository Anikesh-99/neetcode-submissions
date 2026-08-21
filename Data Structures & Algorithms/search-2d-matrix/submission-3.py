class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if matrix[-1][-1] < target or matrix[0][0] > target: return False
        rl, rh = 0, m - 1
        rm = 0
        while rl <= rh:
            rm = rl + (rh - rl)//2
            if matrix[rm][0] <= target <= matrix[rm][-1]:
                break
            if matrix[rm][-1] < target:
                rl = rm + 1
            else:
                rh = rm - 1
        row = matrix[rm]
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r-l)//2
            if target == row[mid]: return True
            if target > row[mid]: l = mid + 1
            else: r = mid - 1
        return False