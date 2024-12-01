class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n  # Array to store the maximum value from the left up to index i
        right_min = [0] * n  # Array to store the minimum value from the right up to index i
        
        # Populate left_max
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        # Populate right_min
        right_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
        
        beauty_sum = 0
        
        # Calculate beauty for each index 1 to n - 2
        for i in range(1, n - 1):
            if left_max[i - 1] < nums[i] < right_min[i + 1]:
                beauty_sum += 2  # Condition for beauty = 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty_sum += 1  # Condition for beauty = 1
        
        return beauty_sum