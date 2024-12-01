class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        # Step 1: Precompute left_max and right_min arrays
        left_max = [0] * n
        right_min = [0] * n

        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
        
        right_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i + 1])
        
        # Step 2: Calculate the sum of beauties
        total_beauty = 0
        for i in range(1, n - 1):
            if left_max[i] < nums[i] < right_min[i]:
                total_beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_beauty += 1
        
        return total_beauty