class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        n2=len(s2)
        n1=len(s1)
        for i in range(n2):
            sub=s2[i:i+n1]
            sub=sorted(sub)
            if sub==s1:
                return True
        return False