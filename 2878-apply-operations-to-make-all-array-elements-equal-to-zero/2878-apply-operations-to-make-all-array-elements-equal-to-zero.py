from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array to track operations
        current_sum = 0  # Tracks how many decrements apply to the current index

        for i in range(n):
            current_sum += diff[i]  # Apply the operations affecting the current index
            if nums[i] - current_sum > 0:
                required_ops = nums[i] - current_sum
                if i + k > n:  # Cannot form a valid subarray of size k
                    return False
                current_sum += required_ops
                diff[i + k] -= required_ops  # Undo the effect of operations after k elements
            elif nums[i] - current_sum < 0:
                return False  # Unreachable since nums[i] can't be negative

        return True