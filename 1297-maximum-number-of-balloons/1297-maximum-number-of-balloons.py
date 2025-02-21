class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s="balloon"
        dici={}
        for i in text:
            if i in s:
                if i not in dici:
                    dici[i]=1
                else:
                    dici[i]+=1
        if len(dici)!=5:
            return 0
        return(min(dici['b'],dici['a'],dici['l']//2,dici['o']//2,dici['n']))