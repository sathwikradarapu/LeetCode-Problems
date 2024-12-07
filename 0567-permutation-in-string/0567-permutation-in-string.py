class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        n1=len(s1)
        n2=len(s2)
        temp1=""
        s1=sorted(s1)
        for r in range(n2):
            temp1+=s2[r]
            if r-l==n1:
                temp1=temp1[1:]
                l+=1
            if r-l+1==n1:
                temp2=temp1
                temp2=sorted(temp2)
                if temp2==s1:
                    return True
        return False