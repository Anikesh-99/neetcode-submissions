class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhm, colhm = defaultdict(set), defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                if board[i][j] in rowhm[i] or board[i][j] in colhm[j]: return False
                rowhm[i].add(board[i][j])
                colhm[j].add(board[i][j])
        def checksubbox(startx, starty):
            st = set()
            for i in range(startx, startx + 3):
                for j in range(starty, starty + 3):
                    if board[i][j] == ".": continue
                    if board[i][j] in st: 
                        return False
                    st.add(board[i][j])
            return True
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not checksubbox(i, j): return False
        return True