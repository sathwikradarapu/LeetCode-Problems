class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={i:set() for i in range(9)}
        column={i:set() for i in range(9)}
        box={i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                ele=board[i][j]
                if ele!='.':
                    if ele in row[i]:
                        return False
                    else:
                        row[i].add(ele)
        for j in range(9):
            for i in range(9):
                ele=board[i][j]
                if ele!='.':
                    if ele in column[j]:
                        return False
                    else:
                        column[j].add(ele)
        for i in range(9):
            for j in range(9):
                ele=board[i][j]
                if ele!='.':
                    index=3*(i//3)+(j//3)
                    if ele in box[index]:
                        return False
                    else:
                        box[index].add(ele)
        return True
            