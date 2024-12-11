from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # Handle empty input
            return 0

        n = len(height)
        total_water = 0
        
        # Precompute the maximum heights to the left and right of each bar
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate trapped water
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                total_water += water_level - height[i]
        
        return total_water
