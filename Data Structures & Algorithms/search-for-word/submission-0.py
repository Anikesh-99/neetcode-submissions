class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from functools import reduce
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def check(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])
        ans = False
        def backtrack(x, y, idx):
            if idx == len(word): return True
            if not check(x, y) or word[idx] != board[x][y] or used[x][y]: return False
            used[x][y] = True
            res = reduce(lambda x, y: x or y, [backtrack(x + i, y + j, idx + 1) for i, j in dirs])
            # res = (backtrack(x + 1, y, idx + 1) or
            #        backtrack(x, y + 1, idx + 1) or
            #        backtrack(x, y - 1, idx + 1) or
            #        backtrack(x - 1, y, idx + 1))
            used[x][y] = False
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0): return True
        return False
            