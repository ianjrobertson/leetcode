class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            row_set = set()
            for col in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_set:
                    return False
                row_set.add(board[row][col])
        
        for col in range(0,9):
            col_set = set()
            for row in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in col_set:
                    return False
                col_set.add(board[row][col])
             
        for start_row in range(0,9,3):
            for start_col in range(0,9,3):
                box_set = set()
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in box_set:
                            return False
                        box_set.add(board[row][col])

        return True
