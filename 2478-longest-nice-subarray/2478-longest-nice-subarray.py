class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bitmask = 0  # Tracks the OR of the current subarray
        max_length = 0

        for right in range(len(nums)):
            while (bitmask & nums[right]) != 0:  # If new element violates "nice" condition
                bitmask ^= nums[left]  # Remove nums[left] from current bitmask
                left += 1  # Shrink window
            
            bitmask |= nums[right]  # Add nums[right] to the current bitmask
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length