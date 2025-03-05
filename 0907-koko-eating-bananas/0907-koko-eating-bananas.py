from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # Search space: [1, max pile size]
        result = right  # Initialize result with max value

        while left <= right:
            mid = (left + right) // 2  # Middle eating speed
            total_hours = sum(math.ceil(pile / mid) for pile in piles)  # Compute required hours
            
            if total_hours <= h:  # Can finish within h hours
                result = mid  # Update result
                right = mid - 1  # Try to minimize k
            else:
                left = mid + 1  # Increase speed
            
        return result
