class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={i:set() for i in range(9)}
        col={i:set() for i in range(9)}
        box={i:set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                ele=board[i][j]
                if ele!='.':
                    index=3*(i//3)+(j//3)
                    if ele in row[i] or ele in col[j] or ele in box[index]:
                        return False
                    row[i].add(ele)
                    col[j].add(ele)
                    box[index].add(ele)
        return True