class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        start = 0
        max_length = 1
        
        for i in range(n):
            for j in range(i, n):
                # Check if the current window s[i:j+1] is a palindrome
                if s[i:j+1] == s[i:j+1][::-1]:
                    current_length = j - i + 1
                    if current_length > max_length:
                        start = i
                        max_length = current_length
        
        return s[start:start + max_length]
