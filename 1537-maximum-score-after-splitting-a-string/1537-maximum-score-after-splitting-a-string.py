class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        ans=float("-inf")
        for i in range(1,n):
            zero=s[:i].count("0")
            one=s[i:].count("1")
            ans=max(ans,zero+one)
        return ans