class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0  # Edge case, if k is larger than the array length

        max_sum = 0
        current_sum = 0
        seen = set()
        
        left = 0  # Left pointer for sliding window
        
        for right in range(n):
            while nums[right] in seen or len(seen) >= k:
                # Remove element at 'left' from window
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add new element to the window
            seen.add(nums[right])
            current_sum += nums[right]
            
            if len(seen) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum