class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhm, colhm, boxhm = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                if board[i][j] in rowhm[i]: return False
                if board[i][j] in colhm[j]: return False
                if board[i][j] in boxhm[i//3 * 3 + j//3]: return False
                rowhm[i].add(board[i][j])
                colhm[j].add(board[i][j])
                boxhm[i//3 * 3 + j // 3].add(board[i][j])
        return True