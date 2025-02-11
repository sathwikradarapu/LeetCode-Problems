class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(t)
        m=len(s)
        i=0
        j=0
        count=0
        while i<n and j<m:
            if t[i]==s[j]:
                count+=1
                j+=1
            i+=1
        if count==m:
            return True
        return False