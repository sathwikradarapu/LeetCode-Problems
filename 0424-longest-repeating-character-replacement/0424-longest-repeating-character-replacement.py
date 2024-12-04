class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        char_count = {}
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            max_count = max(max_count, char_count[char])

            # Current window size is (right - left + 1)
            # If we need to replace more than k characters to make all characters same
            if (right - left + 1) - max_count > k:
                # Shrink the window
                char_count[s[left]] -= 1
                left += 1

            # Update max_length
            max_length = max(max_length, right - left + 1)
        
        return max_length