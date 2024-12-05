class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            # Count zeros in the current window
            if nums[right] == 0:
                zero_count += 1
            
            # If there's more than one zero, move the left pointer
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the max length excluding one element
            max_length = max(max_length, right - left+1)
        
        return max_length-1