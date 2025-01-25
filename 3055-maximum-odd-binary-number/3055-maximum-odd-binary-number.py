class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str: 
        dici={}
        for i in s:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        if len(dici)==1:
            return s
        else:
            if dici['1']==1:
                zero='0'*dici['0']
                return zero+'1'
            else:
                dici['1']-=1
                one='1'*dici['1']
                zero='0'*dici['0']
                return one+zero+'1'