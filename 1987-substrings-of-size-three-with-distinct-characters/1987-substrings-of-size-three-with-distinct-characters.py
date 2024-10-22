class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        v=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if len(t)==3:
                    u=set(t)
                    if len(u)==3:
                        v+=1
        return v