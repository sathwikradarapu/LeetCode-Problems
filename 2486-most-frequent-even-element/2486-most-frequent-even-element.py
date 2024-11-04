from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash_map = {}
        ans = []
        
        for i in nums:
            if i % 2 == 0:
                if i not in hash_map:
                    hash_map[i] = 1
                else:
                    hash_map[i] += 1

        # Check if hash_map is empty
        if not hash_map:
            return -1

        most_rep = max(hash_map.values())
        
        for i in hash_map:
            if hash_map[i] == most_rep:
                ans.append(i)

        # Return -1 if ans list is empty, else return the minimum value in ans
        return min(ans) if ans else -1
