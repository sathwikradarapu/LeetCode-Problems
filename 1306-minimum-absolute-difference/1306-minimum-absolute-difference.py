from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        result = []
        
        # Step 3: Traverse the sorted array to calculate differences between consecutive elements
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            
            # Update the minimum difference and reset result list if a new minimum is found
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            # If the current difference matches the minimum, add the pair to the result
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result
