class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        s=sorted(s)
        t=sorted(t)
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i]!=t[i]:
                    return False
        return True