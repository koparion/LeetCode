class Solution:
    # Create three sets of sets to store digits seen in each row, column, and 3x3 sub-box.
    # Iterate through each cell in the board.
    # For each cell, check if its digit is already seen in the corresponding row, column, or sub-box. If it is, return False.
    # If all cells pass the checks without any violations, return True.

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize defaultdicts to store seen values in each row, column, and 3x3 sub-box
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        threebythree_squares = collections.defaultdict(set)

        # Iterate through each cell in the Sudoku board
        for row in range(9):
            for col in range(9):
                # Check if the cell is empty
                if board[row][col] == ".":
                    continue  # Skip empty cells

                # Check if the current value is already seen in the same row, column, or 3x3 sub-box
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in threebythree_squares[row // 3, col // 3]):
                    return False  # If duplicate value found, the board is invalid

                # Update sets for the current row, column, and 3x3 sub-box with the current value
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                threebythree_squares[row // 3, col // 3].add(board[row][col])

        # If no duplicate values found, the board is valid
        return True

        ## another method
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # # Iterate through each cell in the board
        # for i in range(9):
        #     for j in range(9):
        #         # Get the current digit
        #         digit = board[i][j]

        #         # Skip checking if the cell is empty
        #         if digit == '.':
        #             continue

        #         # Check if the digit is already seen in the current row
        #         if digit in rows[i]:
        #             return False
        #         rows[i].add(digit)

        #         # Check if the digit is already seen in the current column
        #         if digit in cols[j]:
        #             return False
        #         cols[j].add(digit)

        #         # Check if the digit is already seen in the current sub-box
        #         box_index = (i // 3) * 3 + j // 3
        #         if digit in boxes[box_index]:
        #             return False
        #         boxes[box_index].add(digit)

        # # If all checks pass, the board is valid
        # return True