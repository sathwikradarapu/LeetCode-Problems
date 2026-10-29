class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''#bruteforce
        length=len(matrix)
        for index in range(length):
            row=matrix[index]
            for item in row:
                if item==target:
                    return True
        return False'''

        #optimise
        length_matrix = len(matrix)

        for index in range(length_matrix):
            row = matrix[index]
            length_row = len(row)

            left = 0
            right = length_row - 1

            while left <= right:  # Bug 1 fixed
                middle = (left + right) // 2

                if row[middle] == target:
                    return True
                elif target > row[middle]:
                    left = middle + 1
                else:
                    right = middle - 1  # Bug 2 fixed

        return False  # Move outside the for loop
            