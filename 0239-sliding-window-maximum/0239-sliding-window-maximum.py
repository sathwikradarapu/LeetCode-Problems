from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * (n - k + 1)
        deq = deque()

        for i in range(n):
            # Remove indices that are out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove indices whose corresponding values are less than nums[i]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add the current index to the deque
            deq.append(i)

            # Add the maximum element of the current window to the result
            if i >= k - 1:
                result[i - k + 1] = nums[deq[0]]

        return result
