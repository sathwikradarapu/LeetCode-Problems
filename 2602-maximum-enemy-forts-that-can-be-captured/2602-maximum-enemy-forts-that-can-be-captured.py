from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        last = None

        for i in range(len(forts)):
            # Check when we encounter a fort occupied by an army (1 or -1)
            if forts[i] == 1 or forts[i] == -1:
                # If there's a previous fort position, calculate the distance
                if last is not None and forts[i] != forts[last]:
                    ans = max(ans, i - last - 1)
                # Update last position
                last = i

        return ans
