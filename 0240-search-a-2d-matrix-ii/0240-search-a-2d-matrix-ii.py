class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bruteforce
        length=len(matrix)
        for index in range(length):
            row=matrix[index]
            for item in row:
                if item==target:
                    return True
        return False