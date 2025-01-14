class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dici = {}
        max_length = -1
        
        for i, char in enumerate(s):
            if char in dici:
                # Update max_length by calculating the length between current and first occurrence
                max_length = max(max_length, i - dici[char] - 1)
            else:
                # Store the first occurrence index of the character
                dici[char] = i
        
        return max_length
