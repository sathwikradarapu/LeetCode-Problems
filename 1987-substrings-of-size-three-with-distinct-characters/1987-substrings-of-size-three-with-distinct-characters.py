class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        l=0
        temp=""
        k=3
        c=0
        for r in range(n):
            temp+=s[r]
            if r-l==k:
                temp=temp[1:]
                l+=1
            if r-l+1==k:
                if len(set(temp))==k:
                    c+=1
        return c