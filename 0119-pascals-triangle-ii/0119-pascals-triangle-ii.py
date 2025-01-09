class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            # Start with the first row
            l = [[1]]
            for i in range(1, rowIndex + 1):
                # Create a new row with 1 at both ends
                new_row = [1] * (i + 1)
                # Fill the inner elements as the sum of the two elements above
                for j in range(1, i):
                    new_row[j] = l[-1][j - 1] + l[-1][j]
                # Append the new row to the list
                l.append(new_row)
            return l[rowIndex]