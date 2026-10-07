class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_square = set()
            q_i,r_i = divmod(i,3)
            for j in range(9):
                q_j,r_j = divmod(j,3)
                if board[i][j] in seen_row and board[i][j] != '.':
                    return False
                if board[j][i] in seen_col and board[j][i] != '.':
                    return False
                if board[q_i*3 + q_j][r_i*3 + r_j] in seen_square and board[q_i*3 + q_j][r_i*3 + r_j] != '.':
                    return False
                seen_row.add(board[i][j])
                seen_col.add(board[j][i])
                seen_square.add(board[q_i*3 + q_j][r_i*3 + r_j])
        return True