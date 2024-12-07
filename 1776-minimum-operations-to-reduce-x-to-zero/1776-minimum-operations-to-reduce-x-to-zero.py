class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1  # Impossible to achieve

        n = len(nums)
        current_sum = 0
        max_window_size = -1
        left = 0

        # Sliding window to find the longest subarray with sum = target
        for right in range(n):
            current_sum += nums[right]

            # Shrink the window if the current_sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Check if the current window matches the target sum
            if current_sum == target:
                max_window_size = max(max_window_size, right - left + 1)

        # If a valid subarray is found, return the number of operations
        return n - max_window_size if max_window_size != -1 else -1
