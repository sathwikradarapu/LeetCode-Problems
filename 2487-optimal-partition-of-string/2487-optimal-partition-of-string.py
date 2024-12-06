class Solution:
    def partitionString(self, s: str) -> int:
        res=0
        sub=''
        for i in s:
            if i in sub:
                sub=''+i
                res+=1
            else:
                sub+=i
        return res+1