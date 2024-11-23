class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = {}
        for row in board:
            digits = {}  # Reset for each row
            for entry in row:
                if entry in ["1","2","3","4","5","6","7","8","9"]:
                    if entry in digits:
                        print("row error!")
                        return False
                    digits[entry] = True

            
            # for cols
            for col_idx in range(9):  # Iterate through columns
                digits = {}  # Reset for each column
                for row_idx in range(9):  # Iterate through rows for the current column
                    val = board[row_idx][col_idx]
                    if val in ["1","2","3","4","5","6","7","8","9"]:
                        if val in digits:
                            print("col error")
                            return False
                        digits[val] = True


            # for sub-boxes
            for box_row in range(0, 9, 3):  # Starting rows of sub-boxes
                for box_col in range(0, 9, 3):  # Starting columns of sub-boxes
                    digits = {}  # Reset for each sub-box
                    for i in range(3):  # Rows in the sub-box
                        for j in range(3):  # Columns in the sub-box
                            val = board[box_row + i][box_col + j]
                            if val in ["1","2","3","4","5","6","7","8","9"]:
                                if val in digits:
                                    print("subbox error")
                                    return False
                                digits[val] = True


        return True

        [["7",".",".",".","4",".",".",".","."],
        [".",".",".","8","6","5",".",".","."],
        [".","1",".","2",".",".",".",".","."],
        [".",".",".",".",".","9",".",".","."],
        [".",".",".",".","5",".","5",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
