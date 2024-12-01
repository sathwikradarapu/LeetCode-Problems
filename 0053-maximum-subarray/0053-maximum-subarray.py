class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to store the maximum sum found so far and the current sum
        max_sum = current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update the current sum by adding the current element, or start a new subarray
            current_sum = max(num, current_sum + num)
            # Update the maximum sum encountered so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum
