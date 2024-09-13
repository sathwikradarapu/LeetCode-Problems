from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = {}
        p_sorted = "".join(sorted(p))  # Sort `p` only once
        for i in range(len(s) - len(p) + 1):  # Fix the range to check the last substring
            new_string = "".join(sorted(s[i:i + len(p)]))  # Sort the current window
            if new_string == p_sorted:
                if new_string not in result:
                    result[new_string]=[i]  # Append the starting index if an anagram is found
                else:
                    result[new_string].append(i)
        for i in result.values():
            return i
