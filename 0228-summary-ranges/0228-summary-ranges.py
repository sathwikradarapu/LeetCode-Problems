from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:  # Edge case: empty list
            return []
        
        c = [nums[0]]  # Start the first range with the first number
        d = []  # This will store all the ranges

        for i in range(n - 1):
            a = nums[i]
            b = nums[i + 1]
            if b == (a + 1):  # Check if the numbers are consecutive
                c.append(b)  # Add the consecutive number to the current range
            else:
                d.append(c)  # Add the current range to the result list
                c = [b]  # Start a new range with the next number

        # Add the last range to the result list
        d.append(c)

        # Format the ranges as strings
        formatted_ranges = []
        for range_list in d:
            if len(range_list) == 1:
                formatted_ranges.append(str(range_list[0]))  # Single number
            else:
                formatted_ranges.append(f"{range_list[0]}->{range_list[-1]}")  # Range

        return formatted_ranges