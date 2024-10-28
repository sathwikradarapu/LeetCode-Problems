from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # Sort and remove duplicates from nums
        nums = sorted(set(nums))
        
        # Calculate initial sum for the first k natural numbers
        result = k * (k + 1) // 2
        
        # Adjust result based on the values in nums
        for num in nums:
            if num <= k:
                # Remove the number from the result sum
                result -= num
                # Add the next smallest number that is not in nums
                k += 1
                # Add the new number to the result sum
                result += k
            else:
                break

        return result
