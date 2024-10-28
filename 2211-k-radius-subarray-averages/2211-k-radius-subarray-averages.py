from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize the result array with -1
        
        # Edge case: if the window size is larger than the array, we can't compute any averages
        if 2 * k + 1 > n:
            return result
        
        # Initial window sum of the first `2 * k + 1` elements
        window_sum = sum(nums[:2 * k + 1])
        
        # Fill the averages starting from the index `k` to `n - k`
        for i in range(k, n - k):
            result[i] = window_sum // (2 * k + 1)
            # Slide the window by subtracting the element that goes out of the window
            # and adding the element that comes into the window
            if i + k + 1 < n:
                window_sum += nums[i + k + 1] - nums[i - k]
        
        return result
