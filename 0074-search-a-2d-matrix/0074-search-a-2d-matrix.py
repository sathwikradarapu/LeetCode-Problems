class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length=len(matrix)
        for i in range(length):
            row=matrix[i]
            left=0
            length_row=len(row)
            right=length_row-1
            while left<=right:
                middle=(left+right)//2
                if row[middle]<target:
                    left=middle+1
                elif row[middle]>target:
                    right=middle-1
                else:
                    return True
        return False