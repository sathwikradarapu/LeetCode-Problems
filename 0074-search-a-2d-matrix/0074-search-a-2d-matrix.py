from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == target:
                    return True
        return False
