from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        length = len(nums)
        left, right = 0, length - 1

        # Step 1: Find the pivot (smallest element)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:  # Pivot is in the right half
                left = middle + 1
            else:  # Pivot is in the left half
                right = middle
        
        pivot = left  # The smallest element's index

        # Step 2: Determine search range
        left, right = 0, length - 1
        if target >= nums[pivot] and target <= nums[right]:  
            left = pivot  # Search in the right half
        else:
            right = pivot - 1  # Search in the left half

        # Step 3: Standard binary search
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1  # Target not found
