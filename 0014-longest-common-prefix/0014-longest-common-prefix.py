from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for i in strs:
            min_length = min(len(i), min_length)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]  # Fixed return statement to correctly slice the prefix
            i += 1
        
        return strs[0][:min_length]  # Added this return statement to handle full prefix cases
