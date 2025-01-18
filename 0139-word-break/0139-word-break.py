from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case for empty string
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # Check if the word fits in the substring starting at i
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:  # If dp[i] becomes True, no need to check further
                    break
        
        return dp[0]


