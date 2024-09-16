class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to keep track of seen numbers
        rows = {i: set() for i in range(9)}       # HashMap for rows
        columns = {j: set() for j in range(9)}    # HashMap for columns
        boxes = {k: set() for k in range(9)}      # HashMap for boxes

        # Checking rows
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
        
        # Checking columns
        for j in range(9):
            for i in range(9):
                num = board[i][j]
                if num != '.':
                    if num in columns[j]:
                        return False
                    columns[j].add(num)
        
        # Checking boxes
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = 3 * (i // 3) + (j // 3)
                    if num in boxes[box_index]:
                        return False
                    boxes[box_index].add(num)

        return True
            