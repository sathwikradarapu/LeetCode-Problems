class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=0
        n=len(num)
        temp=""
        res=[]
        for r in range(n):
            temp+=num[r]
            if r-l==3:
                temp=temp[1:]
                l+=1
            if r-l+1==3:
                sub=set(temp)
                length=len(sub)
                if length==1:
                    sub=list(sub)
                    res.append(sub[0])
        res.sort()
        if res==[]:
            return ""
        else:
            return res[-1]*3
        