class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rh = 0, len(matrix) - 1
        row = -1
        while rl <= rh:
            rm = rl + (rh - rl)//2
            if (rm == 0 and matrix[rm][-1] >= target) or (rm == len(matrix) - 1 and matrix[rm][-1] <= target) or matrix[rm - 1][-1] < target <= matrix[rm][-1]:
                row = rm
                break
            if matrix[rm][-1] < target:
                rl = rm + 1
            else:
                rh = rm - 1
        search = matrix[row]
        # print(search)
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r-l)//2
            if search[m] == target: return True
            if search[m] < target: l = m + 1
            else: r = m - 1
        return False